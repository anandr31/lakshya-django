from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from nurj.views import HomeView, GuidelinesView, EditorialTeamView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^home$',HomeView.as_view(), name='nurj-home'),
	url(r'^guidelines$',GuidelinesView.as_view(), name='nurj-guidelines'),
	url(r'^editorial-team$',EditorialTeamView.as_view(), name='nurj-editorial-team'),
	url(r'^submit$',TemplateView.as_view(template_name="nurj/submit.html")),
    )
