from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import RegistrationForm, RegForm
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template.context import RequestContext
from models import *
from django.views.generic.base import TemplateView

# Create your views here.


def index(request):
    try:
        hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    except Exception, e:
        hackathon=None
        #return render(request, 'hackathon/index.html');
    context = {}
    sponsors = Sponsors.objects.all()
    if hackathon is None:
        context = {'sponsors':sponsors,'finished':'True','Message':'Stay tuned for updates!'}
        return render(request, 'hackathon/index.html',context)
    sponsors = sponsors.filter(hackathon=hackathon)
    context = {'hackathon':hackathon,'sponsors':sponsors}
    return render(request, 'hackathon/index.html', context)

def register(request):
    try:
        hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    except Exception, e:
        hackathon=None;
    if hackathon is None:
        return render_to_response('hackathon/register.html', RequestContext(request,{'finished':'True'}))

    if request.method == 'POST' and request.user.is_authenticated():
        form = RegForm(request.POST)
        if form.is_valid():
            user = request.user
            mobile = form.cleaned_data['mobile']
            team = form.cleaned_data['team']
            problem = form.cleaned_data['problem']
            year = form.cleaned_data['year']
            course = form.cleaned_data['course']
            branch = form.cleaned_data['branch']
            mess = form.cleaned_data['mess']
            roll_no = form.cleaned_data['roll_no']
            tee = form.cleaned_data['tee']
            gender = form.cleaned_data['gender']

            participant = Participant(name=name,mobile=mobile,team=team,email=email,problem=problem,year=year,course=course,
                                      branch=branch,mess=mess,roll_no=roll_no,tee_shirt_size=tee,gender=gender,hackathon=hackathon)

            participant.save()

            return render_to_response('hackathon/success.html', RequestContext(request,{'name':name}))
        else:
            render_to_response('hackathon/register.html',RequestContext(request,{'form':form}))
    try:
        problem = ProblemStatement.objects.all().filter(is_active=True)[0]
    except Exception,e:
        problem = None
    if problem is None:
        form = RegForm()
    else:
        form = RegForm(initial = {'problem':problem})
    return render(request,'hackathon/register.html',{'form':form})

def get_email(request):
    if request.user.is_superuser:
        participants = Participant.objects.all()
        emails = []
        for participant in participants:
            emails.append(participant.user.email)

        return render(request,"hackathon/emails.html",{'emails':emails})
    else:
        return HttpResponseRedirect('/admin/')

def get_email_by_prob_statement(request,problem_id):
    if request.user.is_superuser:
        participants = Participant.objects.all().filter(problem_id=problem_id)
        emails = []
        for participant in participants:
            emails.append(participant.user.email)

        return render(request,"hackathon/emails.html",{'emails':emails})
    else:
        return HttpResponseRedirect('/admin/')

def problems(request):
    try:
        hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    except Exception, e:
        hackathon = None
    
    if hackathon is None:
        problem_sts = ProblemStatement.objects.all()
    else:
        problem_sts = ProblemStatement.objects.all().filter(hackathon=hackathon)
    context = {'problems':problem_sts}
    return render(request, 'hackathon/problems.html',context)

def get_problem_statement(request,problem_id):
    problem = get_object_or_404(ProblemStatement,pk=problem_id)
    context = {'problem':problem}
    return render(request,'hackathon/problem_statement.html',context)

def faq(request):
    hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    if hackathon is None:
        return render(request,'hackathon/faq.html')
    else:
        return render(request,'hackathon/faq.html',{'hackathon':hackathon})

def student_details(request):
    if request.user.is_superuser:
        participants = Participant.objects.all()
        return render(request,'hackathon/students.html',{'students':participants})
    else:
        return HttpResponseRedirect('/admin')


class HackathonHomeView(TemplateView):
    template_name = 'hackathon/home.html'
