from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('nem.views',
    url(r'^/?$', 'show_home'),

)