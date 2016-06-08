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
from lakshya.util import send_email_from_template
from people.models import Person
from django.contrib.auth.models import User

logger = logging.getLogger('GROUPIFY')


class PGTransactionView(TemplateView):
    template_name = 'paymentgateway/transaction.html'

    def get_context_data(self, **kwargs):
        context = super(PGTransactionView, self).get_context_data(**kwargs)
        txnid = kwargs['txnid'].replace('/', '')
        context['txn'] = txn = self.get_txn(txnid)
        gateway = get_gateway_object('ccavenue')  # Later it could be dynamic.
        gateway.set_form_context(context, self.request, txn)
        return context

    def get_txn(self, txnid):
        try:
            txn = PGTransaction.objects.get(txnid=txnid)
        except PGTransaction.DoesNotExist:
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
        txnid = gateway.get_txn_id_from_response_data(data)
        txn = self.get_txn(txnid)
        txn.response_data = json.dumps(data)
        txn.save()

        if not gateway.verify_response(data, txn):
            txn.status = PGTransaction.TS_ERROR
        else:
            gateway.update_txn(data, txn)
        txn.save()
        user = User.objects.get(email=txn.email)
        person = Person.objects.get(user=user)
        context = {'txn': txn, 'person': person}
        txn.content_object.on_payment_response(txn)
        txn.content_object.populate_context(context)
        if txn.status == PGTransaction.TS_SUCCESS:
            subject = 'Thank you!'
            email_context = {'amount': txn.amount, 'name': person.name()}
            #Send email to donor
            send_email_from_template('emails/fcra_thank_you.html', email_context, subject, txn.email)

        return render(request, self.template_name, context)

    def get_txn(self, txnid):
        try:
            return PGTransaction.objects.get(txnid=txnid)
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
