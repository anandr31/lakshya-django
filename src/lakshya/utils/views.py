from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext

from utils.models import LakshyaUpdate
from accounts.models import Donation
from people.models import Person
from django.db.models.aggregates import Sum
from django.contrib.auth.models import User

def get_updates(request):
    update_list = LakshyaUpdate.objects.order_by('-date_of_entry')  
    print update_list
    return render_to_response("all_updates.html", 
                              RequestContext(request, {'update_list':update_list}))# Create your views here.
    
@staff_member_required
def get_donation_details_for_analytics(request):
    context = {}
    separator = "|"
    if request.GET and request.GET["separator"]:
        separator = request.GET["separator"]
    context["separator"] = separator
    
    donor_details_list = [] #list of tuples - name, batch, branch, amount, last Donated on
    for temp_dict in Donation.objects.values('donor').annotate(total=Sum('amount')):
        donor_id = temp_dict["donor"]
        total = temp_dict["total"]
        donor = Person.objects.get(id=donor_id)
        last_donated_on = Donation.objects.filter(donor = donor).order_by("-date_of_donation")[0].date_of_donation
        donor_details = (donor.name, donor.year_of_passing, donor.get_department_display, total, last_donated_on.strftime("%d-%m-%Y"))
        donor_details_list.append(donor_details)
    
    context['donor_details_list'] = donor_details_list
    return render_to_response("get-donation-details-for-analytics.html", 
                              RequestContext(request, context))   
    
@staff_member_required
def get_donor_emails_for_campaigns(request):    
    emails = [ user.email for user in User.objects.filter(person__donation__isnull=False).distinct() if user.email]
    return render_to_response("get-donor-emails-for-campaigns.html", 
                              RequestContext(request, {"email_addresses" : ", ".join(emails)}))
             

