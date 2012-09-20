from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from utils.models import LakshyaUpdate

def get_updates(request):
    update_list = LakshyaUpdate.objects.order_by('-date_of_entry')  
    print update_list
    return render_to_response("all_updates.html", 
                              RequestContext(request, {'update_list':update_list}))# Create your views here.
