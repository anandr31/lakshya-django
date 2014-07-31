from forms import RegistrationForm, RegForm
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from models import *

# Create your views here.

def index(request):
    return render(request, 'hackathon/index.html', {})

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            team = form.cleaned_data['team']
            email = form.cleaned_data['email']
            problem = form.cleaned_data['problem']

            participant = Participant(name=name,mobile=mobile,team=team,email=email,problem=problem)
            participant.save()

            return render_to_response("hackathon/success.html", RequestContext(request,{'name':name}))
        else:
            return render_to_response("hackathon/register.html", RequestContext(request, {'form' : form}))

    form = RegForm()
    return render(request,'hackathon/register.html',{'form':form})