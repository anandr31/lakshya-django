import datetime
import textwrap

from django.contrib import admin
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import Http404, HttpResponseNotFound

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
    p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/receipt-header.jpg", 2, 720, 600, 100)
    p.drawString(20, 680, datetime.date.today().strftime("%B %d, %Y"))
    p.drawString(430, 680, "No. "+str(donation.receipt_number) + "/" + get_financial_year(donation))
    p.setFontSize(18)
    p.drawString(200, 650, "Receipt For Donation")
    p.setFontSize(12)
#    import pdb; pdb.set_trace()
    content = '''Received with thanks an amount of Rs.%d (%s only) from %s on %s towards charitable donation vide %s %s (PAN - %s), Address: %s.
    ''' % (donation.amount, number2word.to_card(donation.amount), donation.donor.name(), \
           donation.date_of_donation, donation.get_transacation_type_display(), donation.get_transaction_details(),
           donation.donor.pan_number, donation.donor.get_full_address())
    content_start=620
    for line in textwrap.wrap(content, 100):
        p.drawString(20, content_start, line)
        content_start -= 20
        
    p.drawString(20, 490, "For The Lakshya Foundation")
    p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/managing_trustee_sign.jpg", 20, 440, 80, 35)
    p.drawString(20,430, "Dr K.Padma")
    p.drawString(20, 410, "Managing Trustee")
    p.drawImage(settings.PROJECT_DIR + "/static/img/receipt/receipt_footer.jpg", 2, 180, 600, 230)
    
    p.showPage()
    p.save()
    return "Lakshya-Receipt-Donation-" + str(donation.id) + ".pdf"

def has_insufficient_details(donation):
    has_insufficient_data = False
    data_map = {"amount": donation.amount,
                "name": donation.donor.name,
                "Transaction type": donation.get_transacation_type_display(),
                "Receipt Number": donation.receipt_number,
                "Date of Donation": donation.date_of_donation,
                "Pan Number": donation.donor.pan_number,
                "Full Address": donation.donor.get_full_address(),
                "Email": donation.donor.user.email}
    missing_data_list = []
    for key in data_map.keys():
        if not data_map[key]:
            has_insufficient_data = True
            missing_data_list.append(key)
    return (has_insufficient_data, missing_data_list)
    
def mail_receipt(modeladmin, request, queryset):
    print "adasfdas"
    print request.META['HTTP_HOST']
    for donation in queryset:
        has_insufficient_data, missing_data_list = has_insufficient_details(donation)
        if has_insufficient_data:
            return HttpResponseNotFound("<h3>The below details are missing. So, invoice can't be generated</h3><br>" + 
                                        ",".join(missing_data_list) + "<br><br>" +
                                        '<a href="/admin/accounts/donation/%d">Donation Link</a>  and  <a href="/admin/people/person/%d">Donor Link</a> ' %
                                        (donation.id, donation.donor.id))
        text_content = ('''
Dear %s,

Please find attached the receipt for your donation made to The Lakshya Foundation on %s

Feel free to contact us for any queries. 

Thanks,
Anand
For Lakshya Team
        ''') % (donation.donor.name(), donation.date_of_donation)
        msg = EmailMessage("Lakshya Donation Receipt", text_content, "info@thelakshyafoundation.org", 
                           [donation.donor.user.email,], 
                           bcc=['anand@thelakshyafoundation.org', 'srihari@thelakshyafoundation.org'])
                
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
    
class PledgeOptions(admin.ModelAdmin):
    list_display = ("name", "batch", "rs_or_dollar", "month_of_donation", "donation")
    list_filter = ("rs_or_dollar", "month_of_donation", "batch", )
    
admin.site.register(Expense, ExpenseOptions)
admin.site.register(DonationFund, DonationFundOptions)
admin.site.register(Donation, DonationOptions)
admin.site.register(Pledge, PledgeOptions)