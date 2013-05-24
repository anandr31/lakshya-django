# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def show_home(request):
    context = {"scholar_year_list" : 1, }
    return render_to_response("nem/nem_home.html", 
                              RequestContext(request, context))