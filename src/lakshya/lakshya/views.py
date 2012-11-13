from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from utils.models import LakshyaUpdate
from accounts.models import Donation
from django.db.models import Sum

def get_home_page(request):
    update_list = LakshyaUpdate.objects.filter(sorting__in = [1,2,3]).order_by('sorting')  
    total_donation_amount = Donation.objects.all().aggregate(Sum("amount"))["amount__sum"]
    return render_to_response("index.html", 
                              RequestContext(request, {'update_list':update_list, 'total_donation_amount':total_donation_amount}))# Create your views here.
