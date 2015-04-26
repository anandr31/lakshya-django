from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404
from innovationgarage.models import Project


class IGHomeView(TemplateView):
    template_name = 'ig/home.html'


class IGProjectsView(TemplateView):
    template_name = 'ig/list.html'

class IGProjectDetailView(TemplateView):
    template_name = 'ig/detail.html'

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        id = kwargs.get('id', '')
        try:
        	project = Project.objects.get(id=id)
        except Project.DoesNotExist:
        	raise Http404
        context['project'] = project
        return context
