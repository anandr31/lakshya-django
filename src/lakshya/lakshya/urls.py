from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template' : 'index.html'}, name='home'),
    url(r'^about$', direct_to_template, {'template' : 'about.html'}, name='home'),
    url(r'^team$', direct_to_template, {'template' : 'team.html'}, name='home'),
    url(r'^innovation/', include('innovation.urls')),
    url(r'^scholarships/', include('scholarships.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^asthra/home$', direct_to_template, {'template' : 'asthra_home.html'}, name='home'),
    url(r'^asthra/about$', direct_to_template, {'template' : 'about_asthra.html'}, name='home'),
    url(r'^pilot-projects$', direct_to_template, {'template' : 'pilot_projects.html'}, name='home'),
    url(r'^contact$', direct_to_template, {'template' : 'contact.html'}, name='home'),    
    url(r'^donate$', direct_to_template, {'template' : 'donate.html'}, name='home'),    
    # url(r'^$', 'lakshya.views.home', name='home'),
    # url(r'^lakshya/', include('lakshya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
