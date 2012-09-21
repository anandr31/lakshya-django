# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def get_innovation_list(request, project_name):
    if not project_name:
        project_name = "hovamarine"
    return render_to_response("innovations_list.html", 
                              RequestContext(request, {'project_name':project_name}))# Create your views here.
