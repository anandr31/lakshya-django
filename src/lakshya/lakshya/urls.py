from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from utils.urls import urlpatterns as util_urls
from people.urls import urlpatterns as people_urls
from entrepreneurship.urls import urlpatterns as entrepreneurship_urls
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lakshya.views.get_home_page', name='home'),
    url(r'^about$', direct_to_template, {'template' : 'about.html'}, name='home'),
    url(r'^innovation/', include('innovation.urls')),
    url(r'^scholarships/', include('scholarships.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^asthra/home$', direct_to_template, {'template' : 'asthra_home.html'}, name='home'),
    url(r'^asthra/about$', direct_to_template, {'template' : 'about_asthra.html'}, name='home'),
    url(r'^pilot-projects$', direct_to_template, {'template' : 'pilot_projects.html'}, name='home'),
    url(r'^research/home$', direct_to_template, {'template' : 'research_facilitator_home.html'}, name='research_facilitator_home'),
    url(r'^automation/home$', direct_to_template, {'template' : 'automation_home.html'}, name='automation_home'),    
    url(r'^contact$', direct_to_template, {'template' : 'contact.html'}, name='home'),    
    url(r'^donate$', "accounts.views.donate_home", name='home'),  
    url(r'^seedfund', "accounts.views.seedfund", name='seedfund'),
    url(r'^payment_redirect$', "accounts.views.payment_redirect", name='payment_redirect'),  
    url(r'^payment-return$', "accounts.views.return_view", name='payment-return'),  
    url(r'^payment-success$', direct_to_template, {'template' : 'payment_success.html'}, name='payment-success'),
    url(r'^payment-failure$', direct_to_template, {'template' : 'payment_failure.html'}, name='payment-failure'),
    url(r'^apply$', direct_to_template, {'template' : 'apply-vp.html'}, name='apply-vp'),

       
    # url(r'^$', 'lakshya.views.home', name='home'),
    # url(r'^lakshya/', include('lakshya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += util_urls

urlpatterns += people_urls

urlpatterns += entrepreneurship_urls

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
