import json
import logging

from django.views.generic.base import TemplateView, View
from django.http.response import Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render

# from paymentgateway.models import PGTransaction
from accounts.models import PGTransaction
from paymentgateway.utils import get_gateway_object, get_gateway_class_from_slug

logger = logging.getLogger('GROUPIFY')


class PGTransactionView(TemplateView):
    template_name = 'paymentgateway/transaction.html'

    def get_context_data(self, **kwargs):
        context = super(PGTransactionView, self).get_context_data(**kwargs)
        site_id = self.request.site_id
        txnid = kwargs['txnid'].replace('/', '')
        context['txn'] = txn = self.get_txn(site_id, txnid, self.request.user)
        gateway = get_gateway_object(txn.account)
        gateway.set_form_context(context, self.request, txn)
        context['havedetails'] = txn.has_user_details()
        return context

    def get_txn(self, site_id, txnid, user):
        try:
            txn = PGTransaction.objects(site_id).get(txnid=txnid)
        except PGTransaction.DoesNotExist:
            raise Http404
        # Not current user's transaction or already processed
        if txn.creator != user or txn.status != PGTransaction.TS_UNPROCESSED:
            raise Http404
        return txn

    def post(self, request, **kwargs):
        site_id = request.site_id
        txnid = kwargs['txnid'].replace('/', '')
        name, phone, email = request.POST.get('name', ''), request.POST.get('phone', ''), request.POST.get('email', '')
        txn = self.get_txn(site_id, txnid, request.user)
        self.update_txn(txn, name, email, phone)
        #TODO: Update profile also
        return HttpResponseRedirect(request.path)

    def update_txn(self, txn, name, email, phone):
        txn.name, txn.email, txn.phone = name or txn.name, email or txn.email, phone or txn.phone
        txn.save()


class PGResponseView(TemplateView):
    template_name = 'paymentgateway/response.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PGResponseView, self).dispatch(request, *args, **kwargs)

    def get_gateway(self, **kwargs):
        logger.info("Got a response from payment gateway")
        pg_slug = kwargs.get('pg', '')
        gateway = get_gateway_class_from_slug(pg_slug)
        if not gateway:
            logger.error("Unable to process response. Could not identify the payment gateway parameter [" +
                         pg_slug + "]")
            raise Http404
        return gateway()

    def get(self, request, **kwargs):
        return self.process_response(request, request.GET, self.get_gateway(**kwargs))

    def post(self, request, **kwargs):
        return self.process_response(request, request.POST, self.get_gateway(**kwargs))

    def process_response(self, request, data, gateway):
        site_id = request.site_id
        txnid = gateway.get_txn_id_from_response_data(data)
        txn = self.get_txn(site_id, txnid)
        txn.response_data = json.dumps(data)
        txn.save()
        gateway.update_from_account(txn.account)  # Update merchant ID etc on object to validate response

        #Extra step for some PGs - Get transaction details from server. Eg: Paypal
        new_data = gateway.get_txn_details_from_server(txn, data)
        if new_data:
            data = new_data
            txn.response_data = json.dumps(data)
            txn.save()

        if not gateway.verify_response(data, txn):
            txn.status = PGTransaction.TS_ERROR
        else:
            gateway.update_txn(data, txn)
        txn.save()

        context = {'txn': txn}
        txn.content_object.on_payment_response(txn)
        txn.content_object.populate_context(context)

        return render(request, self.template_name, context)

    def get_txn(self, site_id, txnid):
        try:
            return PGTransaction.objects(site_id).get(txnid=txnid)
        except PGTransaction.DoesNotExist:
            logger.error("Could not find transaction with txnid [" + txnid + "]")
            raise Http404


class PGPostFromServerView(View):
    """Sends a POST request from the server and not from the browser directly.
    Used for PayPal right now"""
    def post(self, request, *args, **kwargs):
        txn = PGTransaction.objects(request.site_id).get_or_none(txnid=request.POST.get('txnid', ''))
        if not txn:
            raise Http404
        gateway = get_gateway_object(txn.account)
        return gateway.process_server_post(request, txn)
