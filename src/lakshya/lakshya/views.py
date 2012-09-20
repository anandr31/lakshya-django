from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from utils.models import LakshyaUpdate

def get_home_page(request):
    update_list = LakshyaUpdate.objects.filter(sorting__in = [1,2,3])  
    return render_to_response("index.html", 
                              RequestContext(request, {'update_list':update_list}))# Create your views here.
