# Create your views here.
#from reportlab.pdfgen import canvas
#from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Sum

from accounts.models import Expense, Donation
from people.models import Person
from accounts.forms import PaymentTempForm
from accounts.models import PaymentTemp
from accounts.utils import get_post_object
from accounts.forms import CCAVenueReturnForm
from django.views.decorators.csrf import csrf_exempt


def expenses_home(request):
    expenses_list = Expense.objects.all()
    context = {"expenses_list" : expenses_list}
    return render_to_response("expenses.html", 
                              RequestContext(request, context))
    
def donations_home(request):
    donor_details_list = [] #list of tuples - name, batch, branch, amount, last Donated on
    for temp_dict in Donation.objects.values('donor').annotate(total=Sum('amount')):
        donor_id = temp_dict["donor"]
        total = temp_dict["total"]
        donor = Person.objects.get(id=donor_id)
        last_donated_on = Donation.objects.filter(donor = donor).order_by("-date_of_donation")[0].date_of_donation
        donor_details = (donor.name, donor.year_of_passing, donor.get_department_display, total, last_donated_on)
        donor_details_list.append(donor_details)
    total_donation_amount = Donation.objects.all().aggregate(Sum("amount"))["amount__sum"]
    donor_distinct_set = set()
    for donation in Donation.objects.all():
        donor_distinct_set.add(donation.donor.id)
    total_donors = len(donor_distinct_set)

    avg_donation_amount = total_donation_amount/total_donors
    
    context = {"donor_details_list" : donor_details_list, 
               "total_donation_amount" : total_donation_amount, 
               "total_donors" : total_donors, 
               "avg_donation_amount" : avg_donation_amount}
    return render_to_response("donations.html", 
                              RequestContext(request, context)) 
    
def donate_home(request):
    form = PaymentTempForm()
    return render(request, 'donate.html', {
        'form': form,
    })
 
def payment_redirect(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PaymentTempForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules passes
            # Process the data in form.cleaned_data
            amount = form.cleaned_data['amount']
            email_address = form.cleaned_data['email_address']
            email_receipt = form.cleaned_data['email_receipt']
            pt = PaymentTemp.objects.create(amount=amount, email_address=email_address, email_receipt=email_receipt)
            transaction_id = pt.id
            callback_url = "http://127.0.0.1:8000/payment-return"
            context = {"payment_dict" : get_post_object(callback_url, amount, email_address, transaction_id)}
            return render_to_response("payment_redirect.html", 
                              RequestContext(request, context))
    else:
        form = PaymentTempForm() # An unbound form

    return render(request, 'donate.html', {
        'form': form,
    })
    
@csrf_exempt
def return_view(request):   
    if request.method == "POST":       
        working_key = "95o6bpj72771v3yo7s"
        merchant_id = "M_thelaksh_10884"
        
        form = CCAVenueReturnForm(merchant_id, working_key, request.POST)
        if not form.is_valid():
            return redirect('payment-failure')
        
       
        if form.cleaned_data['AuthDesc'] == 'N':
            return redirect('payment-failure')
        
        return redirect("payment-success")
    else:
        return redirect('payment-failure')
    
def seedfund(request):
    return render_to_response("seed_fundraising.html", 
                              RequestContext(request, {}))
