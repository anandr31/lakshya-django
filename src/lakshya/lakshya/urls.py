from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
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
    url(r'^about$', TemplateView.as_view(template_name="about.html")),
    url(r'^innovation/', include('innovation.urls')),
    url(r'^research/', include('research.urls')),
    url(r'^scholarships/', include('scholarships.urls')),
    url(r'^accounts/', include('accounts.urls')),
    (r'^notifications/', include('notification.urls')),
    url(r'^asthra/home$',TemplateView.as_view(template_name="ashtra_home.html")),
    url(r'^asthra/about$', TemplateView.as_view(template_name="about_asthra.html")),
    url(r'^pilot-projects$', TemplateView.as_view(template_name="pilot_projects.html")),
    url(r'^automation/home$', TemplateView.as_view(template_name="automation_home.html")),    
    url(r'^contact$',TemplateView.as_view(template_name="contact.html")),    
    url(r'^donate$', "accounts.views.donate_home", name='home'),  
    url(r'^seedfund', "accounts.views.seedfund", name='seedfund'),
    url(r'^payment_redirect$', "accounts.views.payment_redirect", name='payment_redirect'),  
    url(r'^payment-return$', "accounts.views.return_view", name='payment-return'),  
    url(r'^payment-success$',TemplateView.as_view(template_name="payment_success.html")),
    url(r'^payment-failure$', TemplateView.as_view(template_name="payment_failure.html")),
    url(r'^apply$',TemplateView.as_view(template_name="apply-vp.html")),
    url(r'^nem/?$', "nem.views.show_home", name='nem'),  
    url(r'^nem/register/?$', "nem.views.register", name='nem-registration'), 
    url(r'^nem/student/?$', "nem.views.apply_student", name='nem-apply-student'), 
    url(r'^nem/payment-return/?$', "nem.views.return_view", name='nem-payment-return'),    
    url(r'^nem/registration-success/?$', "nem.views.registration_success", name='registration-success'),  
    url(r'^nem/registration-failure/?$', "nem.views.registration_failure", name='registration-failure'),  
    url(r'^corpus$', TemplateView.as_view(template_name="corpus.html")),
    url(r'^newsletter$', TemplateView.as_view(template_name="newsletter.html")),

   
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

handler500 = "lakshya.views.server_error"

