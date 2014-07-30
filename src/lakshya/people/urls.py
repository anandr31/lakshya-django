from django.conf.urls import patterns, include, url
# from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^team$', 'people.views.get_team_details', name='team'),
)
