import datetime
import textwrap
import trml2pdf

from django.contrib import admin
from django.core.mail import EmailMessage
from django.template import loader
from django.template.context import Context
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.conf import settings
from django.http import Http404

from reportlab.pdfgen import canvas

from libraries.num2word import number2word
from accounts.models import Expense, DonationFund, Donation, Pledge


class ExpenseOptions(admin.ModelAdmin):
    list_display = ('amount', 'date_of_expense', 'expense_header_first_level', "expense_header_second_level", "status",)
    list_filter = ('expense_header_first_level', 'expense_header_second_level', "status", )
    date_hierarchy = 'date_of_expense'

class DonationFundOptions(admin.ModelAdmin):
    list_display = ('name', 'description', )

def get_financial_year(donation):
    date=donation.date_of_donation
    months=date.month
    if months<=3:
        return '%d-%d'%(date.year-1,date.year)
    return '%d-%d'%(date.year,date.year+1)


def generate_receipt(donation):
    p = canvas.Canvas("Lakshya-Receipt-Donation-" + str(donation.id) + ".pdf")
    p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/receipt-header.jpg", 2, 700, 600, 133)
    p.drawString(10, 680, datetime.date.today().strftime("%B %d, %Y"))
    p.drawString(430, 680, "No. "+str(donation.receipt_number) + "/" + get_financial_year(donation))
    p.setFontSize(18)
    p.drawString(200, 650, "Receipt For Donation")
    p.setFontSize(12)
#    import pdb; pdb.set_trace()
    content = '''Received with thanks an amount of Rs.%d (%s only) from %s towards charitable donation vide %s (PAN - %s), %s.
    ''' % (donation.amount, number2word.to_card(donation.amount), donation.donor.name(), \
           donation.get_transacation_type_display(), donation.donor.pan_number, donation.donor.get_full_address())
    content_start=620
    for line in textwrap.wrap(content, 100):
        p.drawString(10, content_start, line)
        content_start -= 20
        
    p.drawString(10, 490, "For The Lakshya Foundation")
    p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/managing_trustee_sign.jpg", 10, 440, 80, 35)
    p.drawString(10,430, "Dr K.Padma")
    p.drawString(10, 410, "Managing Trustee")
    p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/receipt_footer.png", 2, 180, 596, 200)
    
    p.showPage()
    p.save()
    return "Lakshya-Receipt-Donation-" + str(donation.id) + ".pdf"

def has_insufficient_details(donation):
    if donation.amount and donation.donor.name and donation.get_transacation_type_display() and \
        donation.receipt_number and donation.date_of_donation and donation.donor.pan_number and donation.donor.get_full_address() \
        and donation.donor.user.email :
        return False
    return True
    
def mail_receipt(modeladmin, request, queryset):
#    queryset.update(status='p')
    for donation in queryset:
        if has_insufficient_details(donation):
            raise Http404
        text_content = ('''
--------------------************-----------------------
1. Verify the mail content and the attachment
2. Remove this block
3. Forward this to %s after removing the 'Fwd' in the subject header
--------------------************-----------------------

Dear %s,

Please find attached the receipt for your donation made to The Lakshya Foundation on %s

Feel free to contact us for any queries. 

Thanks,
Anand
For Lakshya Team
        ''') % (donation.donor.user.email, donation.donor.name(), donation.date_of_donation)
        msg = EmailMessage("Lakshya Donation Receipt", text_content, "info@thelakshyafoundation.org", 
                           ['srihari@thelakshyafoundation.org',], cc=['sriharimaneru@gmail.com',])
        msg.attach_file(generate_receipt(donation))
        msg.attach_file("static/docs/lakshya_80G_tax_exemption.pdf")
        msg.send()
mail_receipt.short_description = "Mail Receipt"
    
class DonationOptions(admin.ModelAdmin):
    list_display = ('id', 'amount', 'date_of_donation', 'donor', 'receipt_number', )
    list_filter = ('transacation_type', )
    search_fields = ('donor__user__first_name', )
    raw_id_fields = ('donor', 'donation_fund',)
    list_editable = ('receipt_number',)
    actions =[mail_receipt, ]
    
admin.site.register(Expense, ExpenseOptions)
admin.site.register(DonationFund, DonationFundOptions)
admin.site.register(Donation, DonationOptions)
admin.site.register(Pledge)