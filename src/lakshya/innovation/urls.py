from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home$', direct_to_template, {'template' : 'innovation_home.html'}, name='home'),
    url(r'^about-innovation-project$', direct_to_template, {'template' : 'about_innovation_project.html'}, name='about_innnovation_project'),
    url(r'^innovations-list$', direct_to_template, {'template' : 'innovations_list.html'}, name='innovations_list'),
)
