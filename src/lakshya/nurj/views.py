from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from nurj.models import Content
from nurj.constants import CT_ABOUT, CT_GUIDELINES, CT_TEAM

class HomeView(TemplateView):
    template_name = "nurj/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
        	context['about'] = Content.objects.get(type=CT_ABOUT)
        except Content.DoesNotExist:
        	pass
        return context


class GuidelinesView(TemplateView):
    template_name = "nurj/guidelines.html"

    def get_context_data(self, **kwargs):
        context = super(GuidelinesView, self).get_context_data(**kwargs)
        try:
        	context['guidelines'] = Content.objects.get(type=CT_GUIDELINES)
        except Content.DoesNotExist:
        	pass
        return context


class EditorialTeamView(TemplateView):
    template_name = "nurj/editorial.html"

    def get_context_data(self, **kwargs):
        context = super(EditorialTeamView, self).get_context_data(**kwargs)
        try:
        	context['team'] = Content.objects.get(type=CT_TEAM)
        except Content.DoesNotExist:
        	pass
        return context


class SubmissionFormView(TemplateView):
    template_name = "nurj/submit.html"
