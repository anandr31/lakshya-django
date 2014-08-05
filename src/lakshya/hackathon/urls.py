from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from views import *

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^register/?$', register, name='register'),
                       url(r'^emails/?$', get_email, name='emails'),
                       url(r'^problems/?$',problems,name='problems'),
                       url(r'problems/(?P<problem_id>\d+)/?$',get_problem_statement, name='problem_statement'),
                       url(r'faq/?$',faq,name='faq'),
                       )