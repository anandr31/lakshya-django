from django.shortcuts import render, render_to_response
from django.views.generic.base import View, TemplateView
from crowdfunding.models import Project, Pledge, Message
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
        context['projects'] = Project.objects.all
        return context


class ProjectCreateView(TemplateView):

    template_name = 'project/create.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        project = Project.objects.get(id=kwargs.get('id'))
        if project and self.request.user == project.author:
            context['form'] = ProjectForm(instance=project)
            context['mode'] = 'edit'
            context['id'] = project.id
        elif not project:
            context['form'] = ProjectForm()
            context['mode'] = 'create'
        else:
            raise Http404
        return context

    def post(self, request, *args, **kwargs):
        project = Project(author=request.user)
        id = kwargs.get('id')
        if id:
            project = Project.objects.get(id=id)
        form_data = ProjectForm(request.POST, instance=project)
        if form_data.is_valid():
            form_data.save()
            response = {'success':  'true'}
        else:
            response = {'success': 'false'}
        return HttpResponse(json.dumps(response))


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
        project = Project.objects.get(id=kwargs.get('id'))
        context['project'] = project
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
            Pledge.objects.create(user=user, amount=amount, project=project)
            response = {'success': 'true'}
        return HttpResponse(json.dumps(response), content_type="application/json")

    def get_params(self, request):
        errors = []
        try:
            amount = int(request.POST.get('amount', ''))
            if not amount:
                errors.append('Amount cannot be zero')
        except ValueError:
            errors.append(
                'Amount [' + request.POST.get('amount', '') + '] is not a valid integer')

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
