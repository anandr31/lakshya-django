# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings

def show_home(request):
    context = {"nem_base_url" : "http://" + settings.SITE_URL + "/static/nem/", 
               "site_url" : "http://" + settings.SITE_URL + "/",}
    return render_to_response("nem/index.html", 
                              RequestContext(request, context))