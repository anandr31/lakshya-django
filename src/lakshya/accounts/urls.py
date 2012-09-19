from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^our-core-belief$', direct_to_template, {'template' : 'our_core_belief_transparency.html'}, name='our_core_belief'),
    url(r'^donations$', direct_to_template, {'template' : 'donations.html'}, name='donations'),
    url(r'^expenses$', direct_to_template, {'template' : 'expenses.html'}, name='expenses'),
    url(r'^audits$', direct_to_template, {'template' : 'audits.html'}, name='audits'),
)
