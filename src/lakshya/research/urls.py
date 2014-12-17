'''
Created on 14-Jul-2013

@author: srihari
'''
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^home$', TemplateView.as_view(template_name="research_facilitator_home.html")),
    url(r'^about$', TemplateView.as_view(template_name="about_internship_funding.html")),
    url(r'^apply-conference-funding/?$', 'research.views.apply_conference', name="research_apply_conference"),
    url(r'^apply-internship-funding/?$', 'research.views.apply_internship', name="reserach_apply_internship"),
    url(r'^feedback-conference-funding/?$', 'research.views.feedback_conference', name="feedback_conference"),
    url(r'^apply-rfp/?$', TemplateView.as_view(template_name="apply-rfp.html")),
)
