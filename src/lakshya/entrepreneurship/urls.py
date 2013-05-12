from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Examples:
    url(r'^entreprenuers/$', 'entrepreneurship.views.companies_listing',),
    url( r'^company/(?P<company_slug>.*)$', 'entrepreneurship.views.company_detail', name="customization_use_template"),
#    url(r'^expenses$', 'accounts.views.expenses_home',),
)
