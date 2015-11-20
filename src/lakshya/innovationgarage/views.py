from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404
from innovationgarage.models import Project


class IGHomeView(TemplateView):
    template_name = 'ig/home.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
    	projects = Project.objects.all()
        context['projects'] = projects
        return context


class IGProjectsView(TemplateView):
    template_name = 'ig/list.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        projects = Project.objects.all()
        context['projects'] = projects
        return context

        
class IGProjectDetailView(TemplateView):
    template_name = 'ig/detail.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        try:
            project_id = int(kwargs.get('id', ''))
            project = Project.objects.get(id=project_id)
        except (Project.DoesNotExist, ValueError):
            raise Http404
        context['project'] = project
        return context
