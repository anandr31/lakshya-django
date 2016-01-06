from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# from forms import RegistrationForm, RegForm
from forms import RegistrationForm
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template.context import RequestContext
from hackathon.models import *
from django.views.generic.base import TemplateView
from django.http.response import Http404

PREV_HACKATHON_PARTICIPANT_COUNTS = {3: 34, 2: 80, 1: 130}  # Hard coded for now since we dont have all the data


def index(request):
    try:
        hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    except Exception, e:
        hackathon = None
        #return render(request, 'hackathon/index.html');
    context = {}
    sponsors = Sponsors.objects.all()
    if hackathon is None:
        context = {'sponsors':sponsors, 'finished':'True', 'Message':'Stay tuned for updates!'}
        return render(request, 'hackathon/index.html', context)
    sponsors = sponsors.filter(hackathon=hackathon)
    context = {'hackathon':hackathon, 'sponsors':sponsors}
    return render(request, 'hackathon/index.html', context)

def register(request):
    try:
        hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    except Exception, e:
        hackathon = None
    if hackathon is not None:
        registered_user = Participant.objects.all().filter(user=request.user, hackathon=hackathon)
        if registered_user:
            return render_to_response('hackathon/register.html', RequestContext(request, {'registered':'True', 'registered_user':Participant.objects.all().filter(user=request.user, hackathon=hackathon)}))
    if not hackathon:
        return render_to_response('hackathon/register.html', RequestContext(request, {'finished':'True'}))
    if request.method == 'POST' and request.user.is_authenticated():
        # form = RegForm(request.POST)
        form = RegistrationForm(request.POST)
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
            tee = form.cleaned_data['tee_shirt_size']
            gender = form.cleaned_data['gender']

            participant = Participant(hackathon=hackathon, user=user, roll_no=roll_no, year=year, course=course,
                                      branch=branch, mess=mess,  mobile=mobile, problem=problem, team=team, tee_shirt_size=tee, gender=gender, )

            participant.save()

            return render_to_response('hackathon/success.html', RequestContext(request, {'name':user}))
        else:
            render_to_response('hackathon/register.html', RequestContext(request, {'form':form}))
    try:
        problem = ProblemStatement.objects.all().filter(is_active=True)
    except Exception, e:
        problem = None
    if problem is None:
        form = RegistrationForm()
    else:
        form = RegistrationForm()
        form.fields['problem'].queryset = problem
    return render(request, 'hackathon/register.html', {'form':form})

def get_email(request):
    if request.user.is_superuser:
        participants = Participant.objects.all()
        emails = []
        for participant in participants:
            emails.append(participant.user.email)

        return render(request, "hackathon/emails.html", {'emails':emails})
    else:
        return HttpResponseRedirect('/admin/')

def get_email_by_prob_statement(request, problem_id):
    if request.user.is_superuser:
        participants = Participant.objects.all().filter(problem_id=problem_id)
        emails = []
        for participant in participants:
            emails.append(participant.user.email)

        return render(request, "hackathon/emails.html", {'emails':emails})
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
    return render(request, 'hackathon/problems.html', context)

def get_problem_statement(request, problem_id):
    problem = get_object_or_404(ProblemStatement, pk=problem_id)
    context = {'problem':problem}
    return render(request, 'hackathon/problem_statement.html', context)

def faq(request):
    hackathon = Hackathon.objects.all().filter(is_active=True)[0]
    if hackathon is None:
        return render(request, 'hackathon/faq.html')
    else:
        return render(request, 'hackathon/faq.html', {'hackathon':hackathon})

def student_details(request):
    if request.user.is_superuser:
        participants = Participant.objects.all()
        return render(request, 'hackathon/students.html', {'students':participants})
    else:
        return HttpResponseRedirect('/admin')


class HackathonHomeView(TemplateView):
    template_name = 'hackathon/home.html'

    def get_context_data(self, **kwargs):
        context = super(HackathonHomeView, self).get_context_data(**kwargs)
        context['hackathons'] = Hackathon.objects.all().order_by('start_time')
        context['mentors'] = Mentor.objects.all().order_by('-id')[:6]
        sponsors = Sponsor.objects.all().order_by('-id')[:6]
        seen = []
        context['sponsors'] = []
        for sponsor in sponsors:
            if sponsor.name not in seen:
                context['sponsors'].append(sponsor)
                seen.append(sponsor.name)
        
        return context


class HackathonDetailView(TemplateView):
    template_name = 'hackathon/detail.html'

    def get_context_data(self, **kwargs):
        context = super(HackathonDetailView, self).get_context_data(**kwargs)
        try:
            hackathon_id = kwargs.get('id', None)
            context['hackathon'] = hackathon = Hackathon.objects.get(id=hackathon_id)
        except (ValueError, Hackathon.DoesNotExist):
            raise Http404

        if hackathon.id in PREV_HACKATHON_PARTICIPANT_COUNTS:
            context['participant_count'] = PREV_HACKATHON_PARTICIPANT_COUNTS[hackathon.id]
        else:
            context['participant_count'] = hackathon.participants.count()

        context['problem_statements'] = hackathon.problem_statements.order_by('id')
        context['mentors'] = hackathon.mentors.all()
        context['sponsors'] = hackathon.sponsors.all()

        return context
