from forms import ConferenceApplicationForm, InternshipApplicationForm
from django.contrib.auth.models import User
from people.models import Person
from models import ConferenceApplication, InternshipApplication
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from innovation.models import NEED_TO_REVIEW
from datetime import date, datetime
from django.core.mail.message import EmailMessage
from django.conf import settings
from research.forms import ConferenceApplicationFeedbackForm
from django.http import Http404
from research.models import Panelist, ConferenceApplicationFeedback


def apply_conference(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ConferenceApplicationForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules passes
            try:
                user = User.objects.filter(email=form.cleaned_data['email'])[0]
            except :
                user = User.objects.create(username=form.cleaned_data['email'],first_name=form.cleaned_data['name'], 
                                           email=form.cleaned_data['email'])    
            
            #A dirty hack till we support logins and sessions in our system. @author: srihari
            #To avoid corrupting the person's data of someone else by entering their email id
            try:
                person = Person.objects.get(user=user)
                person.billing_address = person.billing_address + str(form.cleaned_data)
                person.save()
            except Person.DoesNotExist:
                person = Person.objects.create(user=user, contact_number=form.cleaned_data['contact_number'],
                                               is_nitw_alumni=True, course=form.cleaned_data['course'],
                                               department=form.cleaned_data['department'],
                                               year_of_passing=form.cleaned_data['year_of_passing'])
            ca = ConferenceApplication.objects.create(date_of_submission=date.today(), 
                                                 year_of_submission=date.today().year,
                                                 applicant=person,
                                                 conference_name=form.cleaned_data['conference_name'],
                                                 conference_dates=form.cleaned_data['conference_dates'],
                                                 conference_city=form.cleaned_data['conference_city'],
                                                 conference_country=form.cleaned_data['conference_country'],
                                                 conference_url=form.cleaned_data['conference_url'],                                                 
                                                 expected_expenditure=form.cleaned_data['expected_expenditure'],
                                                 paper_title=form.cleaned_data['paper_title'],
                                                 research_paper=form.cleaned_data['research_paper'],
                                                 sop=form.cleaned_data['sop'],
                                                 acceptance_email=form.cleaned_data['acceptance_email'],)
            
#            import pdb; pdb.set_trace()
            for panelist in Panelist.objects.filter(branch=form.cleaned_data['department'], active=True):
                print "************" + panelist.email
                content = """
Dear %s
Please review the below application
Conference Name : %s
Paper Title : %s
Feedback Link : %s
""" % (panelist.name,ca.conference_name, ca.paper_title, 
                       "%s/research/feedback-conference-funding?application_id=%d&panelist_id=%d" % (settings.SITE_URL, ca.id, panelist.id))
                msg = EmailMessage("Lakshya: Feedback on conference funding application", content, "info@thelakshyafoundation.org", 
                               [panelist.email,],)
                msg.attach_file(settings.MEDIA_ROOT +"/"+ ca.research_paper.name)
                msg.attach_file(settings.MEDIA_ROOT +"/"+ ca.sop.name)
                msg.attach_file(settings.MEDIA_ROOT +"/"+ ca.acceptance_email.name)
                msg.send()            
            
            return render_to_response("apply_research_success.html", RequestContext(request, {}))
    else:
        form = ConferenceApplicationForm() # An unbound form

    return render(request, 'apply_conference.html', {
        'form': form,
    })

def apply_internship(request):
    if request.method == 'POST': # If the form has been submitted...
        form = InternshipApplicationForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules passes
            try:
                user = User.objects.filter(email=form.cleaned_data['email'])[0]
            except:
                user = User.objects.create(username=form.cleaned_data['email'],first_name=form.cleaned_data['name'], 
                                           email=form.cleaned_data['email'])    
            
            #A dirty hack till we support logins and sessions in our system. @author: srihari
            #To avoid corrupting the person's data of someone else by entering their email id
            try:
                person = Person.objects.get(user=user)
                person.billing_address = person.billing_address + str(form.cleaned_data)
                person.save()
            except Person.DoesNotExist:
                person = Person.objects.create(user=user, contact_number=form.cleaned_data['contact_number'],
                                               is_nitw_alumni=True, course=form.cleaned_data['course'],
                                               department=form.cleaned_data['department'],
                                               year_of_passing=form.cleaned_data['year_of_passing'])
            InternshipApplication.objects.create(date_of_submission=date.today(), 
                                                 year_of_submission=date.today().year,
                                                 applicant=person,
                                                 internship_place=form.cleaned_data['internship_place'],
                                                 internship_division=form.cleaned_data['internship_division'],
                                                 supervisor_name=form.cleaned_data['supervisor_name'],
                                                 internship_dates=form.cleaned_data['internship_dates'],
                                                 internship_city=form.cleaned_data['internship_city'],
                                                 internship_country=form.cleaned_data['internship_country'],
                                                 expected_expenditure=form.cleaned_data['expected_expenditure'],
                                                 sop=form.cleaned_data['sop'],)
            return render_to_response("apply_research_success.html", RequestContext(request, {}))
    else:
        form = InternshipApplicationForm() # An unbound form

    return render(request, 'apply_internship.html', {
        'form': form,
    })
    
    
def feedback_conference(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ConferenceApplicationFeedbackForm(request.POST, request.FILES) # A form bound to the POST data
        ca = ConferenceApplication.objects.get(id=form.cleaned_data['application_id'])
#        import pdb; pdb.set_trace()
        if form.is_valid(): # All validation rules passes
            caf = ConferenceApplicationFeedback.objects.create(application=ConferenceApplication.objects.get(id=form.cleaned_data['application_id']),
                                                         panelist=Panelist.objects.get(id=form.cleaned_data['panelist_id']),
                                                         conference_quality=form.cleaned_data['conference_quality'],
                                                         paper_quality=form.cleaned_data['paper_quality'],
                                                         significance_of_contribution=form.cleaned_data['significance_of_contribution'],
                                                         originality_of_content=form.cleaned_data['originality_of_content'],
                                                         technical_quality=form.cleaned_data['technical_quality'],
                                                         recommended_extent_of_funding=form.cleaned_data['recommended_extent_of_funding'],
                                                         feedback=form.cleaned_data['feedback'],
                                                         time_stamp=datetime.now())
            
            content = """
            
Hey guys,

We got a feedback for a conference funding application. Below are the details. 

From: %s
For : %s
Application : %s
Application Link : %s 
Feedback Link : %s


""" %(caf.panelist.name, caf.application.paper_title, caf.application.applicant.name(),
      "%s/admin/research/conferenceapplication/%d" % (settings.SITE_URL, caf.application.id), 
      "%s/admin/research/conferenceapplicationfeedback/%d" % (settings.SITE_URL, caf.id))
            msg = EmailMessage("Lakshya: Got feedback on conference funding application", content, "info@thelakshyafoundation.org", 
                               ['srihari@thelakshyafoundation.org', 'anand@thelakshyafoundation.org', 'naveen@thelakshyafoundation.org',],)
            msg.send()
            
            return render_to_response("feedback_conference_success.html", RequestContext(request, {}))
    else: #Need to load a form populating the hidden fields - panelist and application
        if not (request.GET.get("application_id") and  request.GET.get("panelist_id")):
            return render_to_response("feedback_conference_failure.html", RequestContext(request, {}))
        try:
            ca = ConferenceApplication.objects.get(id=request.GET.get("application_id"))
            Panelist.objects.get(id=request.GET.get("panelist_id"))
        except:
            return render_to_response("feedback_conference_failure.html", RequestContext(request, {}))
        context = {"application_id" : request.GET.get("application_id"),
                       "panelist_id": request.GET.get("panelist_id")}
        
        form = ConferenceApplicationFeedbackForm(initial=context) # An unbound form

    return render(request, 'feedback_conference_funding.html', {
        'form': form,
        'conference_application' : ca, 
    })