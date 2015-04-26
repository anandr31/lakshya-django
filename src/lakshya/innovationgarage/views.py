from django.shortcuts import render
from django.views.generic.base import TemplateView


class IGHomeView(TemplateView):
    template_name = 'ig/home.html'


class IGProjectsView(TemplateView):
    template_name = 'ig/list.html'
