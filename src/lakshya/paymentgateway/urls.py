
from django.conf.urls import patterns, include, url
from paymentgateway.views import PGTransactionView, PGResponseView

urlpatterns = patterns('',
    url(r'^transaction/(?P<txnid>.*)/?$', PGTransactionView.as_view(), name="pgtransaction"),
    url(r'^response/(?P<pg>.*)$', PGResponseView.as_view(), name='pg-response'),
)
