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
from accounts.models import FCRADonation
import datetime
import textwrap
from reportlab.pdfgen import canvas
from libraries.num2word import number2word
from django.core.mail import EmailMessage
from django.conf import settings

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
            user = User.objects.get(email=txn.email)
            donor = Person.objects.get(user=user)
            donation = FCRADonation.objects.get(donor=donor, amount=txn.amount, receipt_sent=False)
            self.mail_receipt(donation)
            donation.receipt_sent = True
            donation.save()

        return render(request, self.template_name, context)

    def get_txn(self, txnid):
        try:
            return PGTransaction.objects.get(txnid=txnid)
        except PGTransaction.DoesNotExist:
            logger.error("Could not find transaction with txnid [" + txnid + "]")
            raise Http404

    # send receipt in email... starts here
    def get_financial_year(self, donation):
        date=donation.time.date()
        months=date.month
        if months<=3:
            return '%d-%d'%(date.year-1,date.year)
        return '%d-%d'%(date.year,date.year+1)


    def generate_receipt(self, donation):
        p = canvas.Canvas("Lakshya-FCRA-Donation-Receipt-" + str(donation.id) + ".pdf")
        p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/receipt-header.jpg", 2, 720, 600, 100)
        p.setFontSize(10)
        p.drawString(40, 680, datetime.date.today().strftime("%B %d, %Y"))
        p.drawString(430, 680, "No. "+str(donation.receipt_number) + "/FCRA/" + self.get_financial_year(donation))
        p.setFontSize(18)
        p.drawString(200, 650, "Receipt For Donation")
        p.setFontSize(12)
        content = '''Received with thanks an amount of Rs.%.2f (Rupees %s only) from %s on %s towards charitable donation vide %s, %s.
        ''' % (donation.amount, number2word.to_card(donation.amount), donation.donor.name(), 
               donation.time.date(), donation.get_transacation_type_display(),
               donation.donor.get_full_address())
        content_start=620
        for line in textwrap.wrap(content, 90):
            p.drawString(40, content_start, line)
            content_start -= 20
            
        p.drawString(40, 490, "For The Lakshya Foundation")
        p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/managing_trustee_sign.jpg", 40, 440, 80, 35)
        p.drawString(40,430, "Dr K.Padma")
        p.drawString(40, 410, "Managing Trustee")
        p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/receipt_footer.jpg", 2, 25, 600, 230)
        
        p.showPage()
        p.save()
        print "**************Inside generate_receipt"
        return "Lakshya-FCRA-Donation-Receipt-" + str(donation.id) + ".pdf"

    def mail_receipt(self, donation):

        text_content = ('''
        Dear %s,

        Thank you for donating to Lakshya. Please find attached the receipt for your donation made on %s.

        Please feel free to contact us for any queries.

        Regards,
        The Lakshya Team
                ''') % (donation.donor.name(), donation.time.date())
        msg = EmailMessage("Lakshya Donation Receipt [FCRA]", text_content, "info@thelakshyafoundation.org", 
                           [donation.donor.user.email,], 
                           bcc=['anand@thelakshyafoundation.org'])
                
        msg.attach_file(self.generate_receipt(donation))
        # msg.attach_file("static/docs/lakshya_80G_tax_exemption.pdf")
        msg.send()
        # self.mail_receipt.short_description = "Mail Receipt"
    # ... ends here


class PGPostFromServerView(View):
    """Sends a POST request from the server and not from the browser directly.
    Used for PayPal right now"""
    def post(self, request, *args, **kwargs):
        txn = PGTransaction.objects(request.site_id).get_or_none(txnid=request.POST.get('txnid', ''))
        if not txn:
            raise Http404
        gateway = get_gateway_object(txn.account)
        return gateway.process_server_post(request, txn)
