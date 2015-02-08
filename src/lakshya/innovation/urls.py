from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from innovation.views import InnovationHomeView, InnovationGarageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^home$', direct_to_template, {'template' : 'innovation_home.html'}, name='home'),
    #url(r'^about-innovation-project$', direct_to_template, {'template' : 'about_innovation_project.html'}, name='about_innnovation_project'),
    url(r'^home$', TemplateView.as_view(template_name="innovation_home.html"), name="old-home"),
    url(r'^about-innovation-project$', TemplateView.as_view(template_name="about_innovation_project.html"), name="innovation_project"),
    url(r'^innovations-list(/?)(?P<project_name>.*)$', 'innovation.views.get_innovation_list', name='innovations_list'),
    url(r'^apply/?$', 'innovation.views.apply_innovation', name="innovation_apply"),
    url(r'^newhome/?$', InnovationHomeView.as_view(), name="home"),
    url(r'^ig-home/?$', InnovationGarageView.as_view(), name="Innovation Garage home"),

    )
