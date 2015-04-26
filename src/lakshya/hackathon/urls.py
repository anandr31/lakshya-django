from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from views import *
from hackathon.views import HackathonDetailView

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^newhome/?$', HackathonHomeView.as_view(), name='hackathon-newhome'),
                       url(r'^register/?$', register, name='register'),
                       url(r'^emails/?$', get_email, name='emails'),
                       url(r'^emails/(?P<problem_id>\d+)/?$', get_email_by_prob_statement, name='emails_prob'),
                       url(r'^problems/?$', problems, name='problems'),
                       url(r'problems/(?P<problem_id>\d+)/?$', get_problem_statement, name='problem_statement'),
                       url(r'faq/?$', faq, name='faq'),
                       url(r'students/?$', student_details, name='student'),
                       url(r'^(?P<id>.*)/?$', HackathonDetailView.as_view(), name='hackathon-detail'),
                       )
