from django.shortcuts import render, render_to_response
from django.views.generic.base import View, TemplateView
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
from crowdfunding.forms import ProjectForm
import json
import re
import os
import logging
from django.template.loader import render_to_string
from lakshya.util import send_email_from_template

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
                context['form'] = ProjectForm(instance=project)
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
        form_data = ProjectForm(request.POST, request.FILES.get('project_image', []), instance=project)
        if form_data.is_valid():
            form_data.save()
            if request.FILES.get('project_image', ''):
                images = request.FILES.getlist('project_image')
                for i in images:
                    extension = os.path.splitext(request.FILES['project_image'].name)[1]
                    print extension
                    if not any(extension.lower() in s for s in valid_extensions):
                        print 'Please upload only jpg, png, svg, or jpeg'
                        error = "Please upload only jpg, png, svg, or jpeg"
                    else:
                        project_image = ProjectImage.objects.create(project=project, image=i)
                        print 'Finished uploading images'
            response = {'success': 'true', 'project_id': project.id}
            if self.mode == 'create':
                #Send email to author of the project
                subject = '[NITW Crowdfund] We received your project'
                context = {'project': project, 'request': request}
                send_email_from_template('emails/project_created_author.html', context, subject, project.author.email)
        else:
            response = {'success': 'false'}
        return HttpResponse(json.dumps(response), content_type="application/json")
        # return HttpResponse(json.dumps(response))
                    # return HttpResponseRedirect('/p/' + presentation.slug + '/?k=' + presentation.presenter_key)
        # return render(request, 'home.html', {'error': error})


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
            project = Project.objects.get(id=kwargs.get('id'))
            context['project'] = project
            context['related_projects'] = Project.objects.exclude(id=kwargs.get('id'))[:3]
            user = self.request.user
            if user.is_authenticated() and Pledge.objects.filter(project=project, user=user).exists():
                context['user_pledge'] = Pledge.objects.filter(project=project, user=user).first()
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
                Pledge.objects.create(user=user, amount=amount, project=project)
            response = {'success': 'true'}
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
