from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^our-core-belief$', direct_to_template, {'template' : 'our_core_belief_transparency.html'}, name='our_core_belief'),
    url(r'^donations$', 'accounts.views.donations_home',),
    url(r'^expenses$', 'accounts.views.expenses_home',),
    url(r'^audits$', direct_to_template, {'template' : 'audits.html'}, name='audits'),
    url(r'^payment-return$', 'accounts.views.return_view', name='payment-return'),
    url(r'^payment-failure$', direct_to_template, {'template' : 'payment_failure.html'}, name='payment-failure'),
    url(r'^payment-success$', direct_to_template, {'template' : 'payment_success.html'}, name='payment-success'),
)
