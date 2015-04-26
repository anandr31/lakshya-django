from django.conf.urls import patterns, url

from innovationgarage.views import IGHomeView, IGProjectsView

urlpatterns = patterns('',
                       url(r'^/?$', IGHomeView.as_view(), name='ig-home'),
                       url(r'^projects/?$', IGProjectsView.as_view(), name='ig-projects'),
                    )
