import datetime
import textwrap

from django.contrib import admin
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import Http404, HttpResponseNotFound

from reportlab.pdfgen import canvas

from libraries.num2word import number2word
from accounts.models import Expense, DonationFund, Donation, Pledge
from django.http import HttpResponse


# export expenses to csv
def export_csv_expenses(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Lakshya-Expenses.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Amount"),
        smart_str(u"Date of Expense"),
        smart_str(u"Expense Header"),
        smart_str(u"Expense Subheader"),
        smart_str(u"Details"),
        smart_str(u"Payment Type")
            ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.amount),
            smart_str(obj.date_of_expense),
            smart_str(obj.get_expense_header_first_level_display()),
            smart_str(obj.get_expense_header_second_level_display()),
            smart_str(obj.details),
            smart_str(obj.get_payment_type_display())
        ])
    return response
export_csv_expenses.short_description = u"Export CSV"
#ends here#

class ExpenseOptions(admin.ModelAdmin):
    list_display = ('amount', 'date_of_expense', 'expense_header_first_level', 'expense_header_second_level', 'status', 'details', 'payment_type')
    list_filter = ('expense_header_first_level', 'expense_header_second_level', 'status', 'payment_type', 'amount', 'date_of_expense')
    date_hierarchy = 'date_of_expense'
    actions =[export_csv_expenses]

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
    p.setFontSize(10)
    p.drawString(40, 680, datetime.date.today().strftime("%B %d, %Y"))
    p.drawString(430, 680, "No. "+str(donation.receipt_number) + "/" + get_financial_year(donation))
    p.setFontSize(18)
    p.drawString(200, 650, "Receipt For Donation")
    p.setFontSize(12)
#    import pdb; pdb.set_trace()
    content = '''Received with thanks an amount of Rs.%.2f (Rupees %s only) from %s on %s towards charitable donation vide %s %s (PAN - %s), %s.
    ''' % (donation.amount, number2word.to_card(donation.amount), donation.donor.name(), 
           donation.date_of_donation, donation.get_transacation_type_display(), donation.get_transaction_details(),
           donation.donor.pan_number, donation.donor.get_full_address())
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
    
def is_indirect_donation(donation):
    is_indirect = False
    if donation.donation_type == 0:
	is_indirect = True
    return (is_indirect)

def mail_receipt(modeladmin, request, queryset):
    print "inside mail_receipt()"
    print request.META['HTTP_HOST']
    for donation in queryset:
        has_insufficient_data, missing_data_list = has_insufficient_details(donation)
	is_indirect = is_indirect_donation(donation)
        if is_indirect:
            return HttpResponseNotFound('<p>%d is an <b>indirect donation</b>. Receipt and tax exemption cannot be given.</p>' % donation.id)
        if has_insufficient_data:
            return HttpResponseNotFound("<p>Unable to generate receipt. Below donor details are missing.<p>" + ",".join(missing_data_list) + "<br><br>" + 'Rectify: <a href="/admin/accounts/donation/%d">Donation Link</a>  and  <a href="/admin/people/person/%d">Donor Link</a> ' % (donation.id, donation.donor.id))

        text_content = ('''
Dear %s,

Thank you for donating to Lakshya. Please find attached the donation receipt for your donation made on %s and a copy of 80G approval letter for claiming exemptions as per Income Tax Act.

Please feel free to contact us for any queries.

Regards,
Anand Rajagopalan
The Lakshya Team
        ''') % (donation.donor.name(), donation.date_of_donation)
        msg = EmailMessage("Lakshya Donation Receipt", text_content, "info@thelakshyafoundation.org", 
                           [donation.donor.user.email,], 
                           bcc=['anand@thelakshyafoundation.org', 'srihari@thelakshyafoundation.org'])
                
        msg.attach_file(generate_receipt(donation))
        msg.attach_file("static/docs/lakshya_80G_tax_exemption.pdf")
        msg.send()
mail_receipt.short_description = "Mail Receipt"
    

# export donation to csv
def export_csv_donations(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Lakshya-Donations.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Amount"),
        smart_str(u"Date of Donation"),
        smart_str(u"Donor"),
        smart_str(u"PAN Number"),
        smart_str(u"Receipt Number"),
        smart_str(u"Donation Type"),
        smart_str(u"Transaction Type"),
        smart_str(u"Bank Details"),
        smart_str(u"Transaction Details"),
        smart_str(u"Donor Address"),
        smart_str(u"Donor Contact"),
        smart_str(u"Donor Email")
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.id),
            smart_str(obj.amount),
            smart_str(obj.date_of_donation),
            smart_str(obj.donor.name()),
            smart_str(obj.donor.pan_number),
            smart_str(obj.receipt_number),
            smart_str(obj.get_donation_type_display()),
            smart_str(obj.get_transacation_type_display()),
            smart_str(obj.bank_details),
            smart_str(obj.transaction_details),
            smart_str(obj.donor.get_full_address()),
            smart_str(obj.donor.contact_number),
            smart_str(obj.donor.email())
        ])
    return response
export_csv_donations.short_description = u"Export CSV"
#ends here#

class DonationOptions(admin.ModelAdmin):
    list_display = ('id', 'amount', 'date_of_donation', 'donor', 'receipt_number', 'donation_type', 'transacation_type', 'bank_details', 'transaction_details')
    list_filter = ('transacation_type', 'donation_type', 'donation_fund', 'is_repayment')
    search_fields = ('donor__user__first_name', 'donor__user__last_name', 'donor__user__email', 'id', 'amount', 'receipt_number', 'donation_type', 'transacation_type', 'bank_details', 'transaction_details',)
    raw_id_fields = ('donor', 'donation_fund',)
    list_editable = ('receipt_number',)
    actions =[mail_receipt, export_csv_donations]
    
class PledgeOptions(admin.ModelAdmin):
    list_display = ("name", "batch", "rs_or_dollar", "month_of_donation", "donation")
    list_filter = ("rs_or_dollar", "month_of_donation", "batch", )
    
admin.site.register(Expense, ExpenseOptions)
admin.site.register(DonationFund, DonationFundOptions)
admin.site.register(Donation, DonationOptions)
admin.site.register(Pledge, PledgeOptions)
