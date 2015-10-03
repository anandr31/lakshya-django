from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from crowdfunding.views import ProjectCreateView, ProjectDetailView, ProjectListView, ProjectListAPIView, \
    PledgeCreateAPIView, ProjectDetailAPIView, IndexView, MyProjectsView, BackedProjectsView, ProjectUpdateView, \
    FulfillPledgeView, CrowdFundingPaymentRedirectView, CrowdFundingPaymentReturnView

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='home'),
                       url(r'^projects/?$', ProjectListView.as_view(), name='view all projects'),
                       url(r'^project/create/?$', ProjectCreateView.as_view(mode='create'), name='create project'),
                       url(r'^project/(?P<id>.*)/edit/?$', ProjectCreateView.as_view(mode='edit'), name='edit project'),
                       url(r'^project/(?P<id>.*)/update/?$', ProjectUpdateView.as_view(), name='update project'),
                       url(r'^project/(?P<id>.*)/?$', ProjectDetailView.as_view(), name='view project'),
                       url(r'^_project/list/?$', ProjectListAPIView.as_view(), name='project-list-api'),
                       url(r'^_project/detail/(?P<id>.*)/?$', ProjectDetailAPIView.as_view(),
                           name='project-detail-api'),
                       url(r'^_pledge/create/?$', csrf_exempt(PledgeCreateAPIView.as_view()), name='pledge-create-api'),
                       url(r'^myprojects/?$', MyProjectsView.as_view(), name='myprojects'),
                       url(r'^backedprojects/?$', BackedProjectsView.as_view(), name='backedprojects'),
                       url(r'^faqs/?$', TemplateView.as_view(template_name="crowdfunding/faqs.html"), name='faqs'),
                       url(r'^fulfill-pledge/?$', FulfillPledgeView.as_view(), name='fulfill-pledge'),
                       url(r'^crowdfunding_payment_redirect$', CrowdFundingPaymentRedirectView.as_view(),
                           name='crowdfunding_payment_redirect'),
                       url(r'^payment-return$', csrf_exempt(CrowdFundingPaymentReturnView.as_view()),
                           name='crowdfunding_payment_return'),
                       )
