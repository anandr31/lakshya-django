from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('utils.views',
    # Examples:
    url(r'^updates$', "get_updates", name='updates'),    
)


