from django.shortcuts import render, render_to_response, redirect
from django.views.generic.base import View, TemplateView
from django.conf import settings
from crowdfunding.models import Project, Pledge, Message, ProjectImage
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
import datetime
from django.utils import timezone
from django.template import RequestContext
from django.core.urlresolvers import reverse
from crowdfunding.forms import ProjectForm, ProjectUpdateForm
import json
import re
import os
import logging
import random
import locale
from django.template.loader import render_to_string
from lakshya.util import send_email_from_template, generate_random_string, send_cron_job_emails, send_email_campaign_update_backers, send_email_incomplete_pledges
from accounts.forms import PaymentTempForm, CCAVenueReturnForm
from accounts.models import PaymentTemp
from accounts.util import get_post_object
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
def get_project_json_data(p, request):
    image_urls = [
        'http://' + request.get_host() + url for url in p.get_image_urls()]
    data = {'id': p.id, 'title': p.title, 'summary': p.summary, 'description': p.description,
            'author_name': p.author.get_full_name(), 'goal': p.goal, 'days_remaining': p.days_remaining,
            'video_url': p.video_url, 'team': p.team, 'risks_and_challenges': p.risks_and_challenges,
            'percentage_pledged': p.percentage_pledged, 'pledged_amount': p.pledged_amount,
            'total_backers': p.total_backers, 'image_urls': image_urls,
            'primary_picture_url': p.primary_picture_url}
    return data


class IndexView(TemplateView):
    template_name = 'crowdfunding/home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        context['projects'] = Project.objects.order_by('-created')
        # Get total target funding goal
        total_goal_object = Project.objects.aggregate(Sum('goal')).values()[0]
        total_goal = locale.currency(total_goal_object, grouping=True)
        context['total_goal'] = total_goal.rstrip('0').rstrip('.') #Remove .00

        # Get total pledges made
        total_pledge_object = Pledge.objects.aggregate(Sum('amount')).values()[0]
        total_pledge = locale.currency(total_pledge_object, grouping=True)
        context['total_pledge'] = total_pledge.rstrip('0').rstrip('.') #Remove .00

        return context

class MyProjectsView(TemplateView):
    template_name = 'crowdfunding/myprojects.html'

    def get_context_data(self, **kwargs):
        context = super(MyProjectsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['projects'] = Project.objects.filter(author=self.request.user).order_by('-created')
        else:
            raise Http404
        return context

class BackedProjectsView(TemplateView):
    template_name = 'crowdfunding/backedprojects.html'

    def get_context_data(self, **kwargs):
        context = super(BackedProjectsView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated() and Pledge.objects.filter(user=user).exists():
            context['projects'] = Project.objects.filter(pledges__user=user)

        return context

class ProjectCreateView(TemplateView):
    mode = 'create'
    template_name = 'crowdfunding/project/create.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        if self.mode == 'create':
            context['form'] = ProjectForm()
            context['mode'] = 'create'
        else:
            try:
                project_id = int(kwargs.get('id', ''))
                project = Project.objects.get(id=project_id)
                form = ProjectForm(instance=project)
                # logic for conditional editing
                # Google - How to make read only fields within Django form instance
                if project.is_expired():
                    form.fields['title'].widget.attrs['readonly'] = True
                    form.fields['summary'].widget.attrs['readonly'] = True
                    form.fields['goal'].widget.attrs['readonly'] = True
                    form.fields['period'].widget.attrs['readonly'] = True
                    form.fields['description'].widget.attrs['readonly'] = True
                    form.fields['team'].widget.attrs['readonly'] = True
                    form.fields['risks_and_challenges'].widget.attrs['readonly'] = True
                else:
                    form.fields['title'].widget.attrs['readonly'] = True
                    form.fields['summary'].widget.attrs['readonly'] = True
                    form.fields['goal'].widget.attrs['readonly'] = True
                    form.fields['period'].widget.attrs['readonly'] = True
                context['form'] = form
                context['mode'] = 'edit'
                context['id'] = project.id
                if project.author != self.request.user:
                    raise Http404
            except (Project.DoesNotExist, ValueError):
                raise Http404
        context['mode'] = self.mode
        return context

    def post(self, request, *args, **kwargs):
        valid_extensions = ['.jpg', '.png', '.svg', '.jpeg']
        images = []
        project = Project(author=request.user)
        id = kwargs.get('id', None)
        if id:
            project = Project.objects.get(id=id)
        form_data = ProjectForm(request.POST, request.FILES, instance=project)
        if form_data.is_valid():
            form_data.save()
            if request.FILES.get('project_image', ''):
                images = request.FILES.getlist('project_image')
                for i in images:
                    extension = os.path.splitext(request.FILES['project_image'].name)[1]
                    if not any(extension.lower() in s for s in valid_extensions):
                        error = "Please upload only jpg, png, svg, or jpeg"
                    else:
                        project_image = ProjectImage.objects.create(project=project, image=i)
                        print 'Finished uploading images'
            response = {'success': 'true', 'project_id': project.id}
            if self.mode == 'create':
                #Send email to author of the project
                subject = '[NITW Crowdfund] Your campaign is live!'
                context = {'project': project, 'request': request}
                send_email_from_template('emails/project_created_author.html', context, subject, project.author.email)
            return HttpResponseRedirect(reverse('view project', kwargs={'id': project.id}))
        else:
            response = {'success': 'false', 'errors': form_data.errors}
            print '**********success = false**********'
            print form_data.errors
            print '**********success = false /end**********'
            return HttpResponse(json.dumps(response), content_type="application/json")


class ProjectUpdateView(TemplateView):
    template_name = 'crowdfunding/project/update.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['form'] = ProjectUpdateForm()
        try:
            project_id = int(kwargs.get('id', ''))
            project = Project.objects.get(id=project_id)
            context['project'] = project
            # form = ProjectUpdateForm(instance=project)
            if project.author != self.request.user:
                raise Http404
        except (Project.DoesNotExist, ValueError):
            raise Http404
        # context['mode'] = self.mode
        return context

    def post(self, request, *args, **kwargs):
        # project = Project(author=request.user)
        id = kwargs.get('id', None)
        project = Project.objects.get(id=id)
        form_data = ProjectUpdateForm(request.POST)
        if form_data.is_valid():
            project_update = form_data.save(commit=False)
            project_update.project = project
            project_update.author = request.user
            project_update.save()
            # uncomment below line after testing
            send_email_campaign_update_backers(project)

            # Comment out below lines after testing... starts here
            # send_email_incomplete_pledges(project)
            # send_cron_job_emails()
            # ...ends here
            response = {'success': 'true', 'project_id': project.id}
            return HttpResponseRedirect(reverse('view project', kwargs={'id': project.id}))
        else:
            response = {'success': 'false', 'errors': form_data.errors}
            return HttpResponse(json.dumps(response), content_type="application/json")

class ProjectView(TemplateView):
    template_name = 'project/view.html'


class ProjectListAPIView(View):

    def get(self, request, **kwargs):
        try:
            start = int(request.GET.get('start_index', ''))
            num_projects = int(request.GET.get('num_projects', ''))
            projects = Project.objects.all().order_by(
                'ordering')[start:start + num_projects]
            data = []
            for p in projects:
                data.append(get_project_json_data(p, request))

            response = {'success': 'true', 'projects': data,
                        'total_projects': Project.objects.count()}
        except ValueError:
            response = {'success': 'false', 'projects': []}
        return HttpResponse(json.dumps(response), content_type="application/json")


class ProjectDetailAPIView(View):
    def get(self, request, **kwargs):
        try:
            project_id = int(kwargs.get('id', None))
            project = Project.objects.get(id=project_id)
            response = {'success': 'true', 'project': get_project_json_data(project, request)}
        except ValueError:
            response = {'success': 'false', 'project': {}}
        return HttpResponse(json.dumps(response), content_type="application/json")


class ProjectDetailView(TemplateView):
    template_name = 'crowdfunding/project/detail.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        try:
            related_project_list = []
            for related_project in Project.objects.exclude(id=kwargs.get('id')).order_by('?'):
                if not related_project.is_expired():
                    related_project_list.append(related_project)
            project = Project.objects.get(id=kwargs.get('id'))
            context['project'] = project
            # context['related_projects'] = Project.objects.exclude(id=kwargs.get('id').order_by('?'))[:3]
            context['related_projects'] = related_project_list[:3]
            context['pledges'] = Pledge.objects.filter(project=project).all().order_by('-pledge_fulfilled')
            context['total_pledge_fulfilled'] = Pledge.objects.filter(project=project, pledge_fulfilled=True).count()
            user = self.request.user
            if user.is_authenticated() and Pledge.objects.filter(project=project, user=user).exists():
                # starts here
                context['user_pledge'] = pledge = Pledge.objects.filter(project=project, user=user).first()
                if project.is_expired():
                    # Below code is used if campaign expired and achieved its goal, to help user fulfill pledge
                    payment_temp = PaymentTemp.objects.create(amount=pledge.amount, email_address=pledge.user.email,
                                flex_field="Fulfillment of pledge " + str(pledge.id),
                                referrer_url=self.request.get_full_path(), pledge_id=pledge.id)
                    form = PaymentTempForm(instance=payment_temp)
                    context['form'] = form
                    context['pt_id'] = payment_temp.id
                    # ends here
        except (Project.DoesNotExist, ValueError):
            raise Http404

        return context

class ProjectListView(TemplateView):
    template_name = 'project/list.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['projects'] = Project.objects.all()
        return context


class PledgeCreateAPIView(View):

    def post(self, request, **kwargs):
        amount, user, project, errors = self.get_params(request)
        if errors:
            response = {'success': 'false', 'errors': errors}
        else:
            if Pledge.objects.filter(user=user, project=project).exists():
                #Since a user cannot create multiple pledges for a project, we assume he is editing his current pledge.
                pledge = Pledge.objects.filter(user=user, project=project).first()
                pledge.amount = amount
                pledge.save()
            else:
                pledge = Pledge.objects.create(user=user, amount=amount, project=project)
            response = {'success': 'true'}
            subject = '[NITW Crowdfund] Thank you for pledging!'
            context = {'pledge': pledge, 'request': request}
            #Send email to backer
            send_email_from_template('emails/pledge_created_backer.html', context, subject, pledge.user.email)
            #Send email to author
            subject = '[NITW Crowdfund] New pledge!'
            send_email_from_template('emails/pledge_created_author.html', context, subject, pledge.project.author.email)
            if pledge.project.get_total_pledged_amount() >= pledge.project.goal:
                context = {'project': project, 'request': request}
                subject = '[NITW Crowdfund] Campaign Successfully Funded!'
                send_email_from_template('emails/campaign_successful_author.html', context, subject, pledge.project.author.email)

        return HttpResponse(json.dumps(response), content_type="application/json")

    def get_params(self, request):
        errors = []
        amount = 0
        try:
            amount = int(request.POST.get('amount', ''))
            if amount <= 0:
                errors.append('Amount has to be positive')
        except ValueError:
            errors.append('Amount is not a valid integer')

        if request.user.is_authenticated():
            user = request.user
        else:
            user = None
            try:
                user_id = int(request.POST.get('user_id', ''))
                user = User.objects.get(id=user_id)
            except ValueError:
                errors.append(
                    'User ID [' + request.POST.get('user_id', '') + '] is not a valid integer')
            except User.DoesNotExist:
                errors.append(
                    'No valid user exists with ID [' + request.POST.get('user_id', '') + ']')

        project = None
        try:
            project_id = request.POST.get('project_id', '')
            project = Project.objects.get(id=project_id)
        except ValueError:
            errors.append(
                'Project ID [' + request.POST.get('project_id', '') + '] is not a valid integer')
        except Project.DoesNotExist:
            errors.append(
                'No valid project exists with ID [' + request.POST.get('project_id', '') + ']')

        return (amount, user, project, errors)


class FulfillPledgeView(TemplateView):
    template_name = 'crowdfunding/fulfill_pledge.html'

    def get_context_data(self, **kwargs):
        context = super(FulfillPledgeView, self).get_context_data(**kwargs)
        try:
            context['pledge'] = pledge = Pledge.objects.get(id=pledge_id)
            project_id = pledge.project.id
            project = Project.objects.get(id=project_id)
            print "^&^&*************************^&%^&%^&"
            print project_id
            context['project'] = project
        except (Pledge.DoesNotExist, ValueError):
            raise Http404

        payment_temp = PaymentTemp.objects.create(amount=pledge.amount, email_address=pledge.user.email,
                                flex_field="Fulfillment of pledge " + str(pledge.id),
                                referrer_url=self.request.get_full_path())
        form = PaymentTempForm(instance=payment_temp)
        form.fields['referrer_url'].initial = self.request.get_full_path()
        context['form'] = form
        context['pt_id'] = payment_temp.id
        return context


class CrowdFundingPaymentRedirectView(View):

    def post(self, request, *args, **kwargs):
        form = PaymentTempForm(request.POST)
        referrer_url = form.data['referrer_url']
        print referrer_url
        notes = form.data['flex_field']
        if form.is_valid():  # All validation rules passes
            # Process the data in form.cleaned_data
            amount = form.cleaned_data['amount']
            email_address = form.cleaned_data['email_address']
            try:
                pt_id = int(form.data['pt_id'])
                pt = PaymentTemp.objects.get(id=pt_id)
            except ValueError:
                raise Http404
            transaction_id = pt.id
            if settings.ENV == "stage":
                transaction_id = "stage" + str(pt.id)
            callback_url = "http://www.thelakshyafoundation.org/crowdfunding/payment-return"
            context = {"payment_dict": get_post_object(callback_url, amount, email_address, transaction_id, notes)}
            return render_to_response("payment_redirect.html", RequestContext(request, context))


class CrowdFundingPaymentReturnView(View):
    def post(self, request, *args, **kwargs):
        working_key = "vsb2w5ampye1baft0hg62jlwrscw007u"
        merchant_id = "M_thelaksh_10884"

        form = CCAVenueReturnForm(merchant_id, working_key, request.POST)
        if not form.is_valid():
            return redirect("payment-failure")
        if form.cleaned_data['AuthDesc'] == 'N':
            return redirect("payment-failure")

        try:
            temp_id = request.POST.get("Order_Id")
            # print temp_id
            paymentTemp = PaymentTemp.objects.get(id=temp_id)
            pledge = Pledge.objects.get(id=paymentTemp.pledge_id)
            pledge.pledge_fulfilled = True
            pledge.save()
            # print "Pledge [" + str(pledge.id) + "] has been successfully fulfilled"
            subject = '[NITW Crowdfund] Pledge Fulfilled!'
            context = {'pledge': pledge}
            #Send email to backer
            send_email_from_template('emails/pledge_fulfilled_backer.html', context, subject, pledge.user.email)
            return redirect("/crowdfunding/project/" + str(pledge.project.id))
        except (PaymentTemp.DoesNotExist, Pledge.DoesNotExist):
            print "Error: Shouldn't have come here. PaymentTemp or Pledge record is missing"
            return redirect("payment-success")
        
        return redirect("/crowdfunding/project/" + str(pledge.project.id))