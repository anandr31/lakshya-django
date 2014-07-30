from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from utils.models import LakshyaUpdate
from utils.models import LakshyaTestimonial
from accounts.models import Donation
from django.db.models import Sum

def get_home_page(request):
    update_list = LakshyaUpdate.objects.filter(sorting__in = [1,2,3]).order_by('sorting')  
    total_donation_amount = Donation.objects.all().aggregate(Sum("amount"))["amount__sum"]
    testimonial_list=LakshyaTestimonial.objects.order_by('?')[:3]
    return render_to_response("index.html", 
                              RequestContext(request, {'update_list':update_list, 'total_donation_amount':total_donation_amount, 'testimonial_list':testimonial_list}))# Create your views here.


def server_error(request):
    response = render(request, "500.html")
    response.status_code = 500
    return response
