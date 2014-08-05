from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
            year = form.cleaned_data['year']
            course = form.cleaned_data['course']
            branch = form.cleaned_data['branch']
            mess = form.cleaned_data['mess']
            roll_no = form.cleaned_data['roll_no']
            tee = form.cleaned_data['tee']
            gender = form.cleaned_data['gender']

            participant = Participant(name=name,mobile=mobile,team=team,email=email,problem=problem,year=year,course=course,
                                      branch=branch,mess=mess,roll_no=roll_no,tee_shirt_size=tee,gender=gender)
            participant.save()

            return render_to_response("hackathon/success.html", RequestContext(request,{'name':name}))
        else:
            return render_to_response("hackathon/register.html", RequestContext(request, {'form' : form}))

    form = RegForm()
    return render(request,'hackathon/register.html',{'form':form})

def get_email(request):
    if request.user.is_superuser:
        participants = Participant.objects.all()
        emails = []
        for participant in participants:
            emails.append(participant.email)

        return render(request,"hackathon/emails.html",{'emails':emails})
    else:
        return HttpResponseRedirect('/admin/')

def problems(request):
    return render(request, 'hackathon/problems.html')