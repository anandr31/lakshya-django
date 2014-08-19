from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import RegistrationForm, RegForm
from django.shortcuts import render_to_response, render, get_object_or_404
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

def get_email_by_prob_statement(request,problem_id):
    if request.user.is_superuser:
        participants = Participant.objects.all().filter(problem_id=problem_id)
        emails = []
        for participant in participants:
            emails.append(participant.email)

        return render(request,"hackathon/emails.html",{'emails':emails})
    else:
        return HttpResponseRedirect('/admin/')

def problems(request):
    problem_sts = ProblemStatement.objects.all()
    context = {'problems':problem_sts}
    return render(request, 'hackathon/problems.html',context)

def get_problem_statement(request,problem_id):
    problem = get_object_or_404(ProblemStatement,pk=problem_id)
    context = {'problem':problem}
    return render(request,'hackathon/problem_statement.html',context)

def faq(request):
    return render(request,'hackathon/faq.html')

def student_details(request):
    if request.user.is_superuser:
        participants = Participant.objects.all()
        return render(request,'hackathon/students.html',{'students':participants})
    else:
        return HttpResponseRedirect('/admin')