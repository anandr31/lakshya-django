from forms import ConferenceApplicationForm, InternshipApplicationForm
from django.contrib.auth.models import User
from people.models import Person
from models import ConferenceApplication, InternshipApplication
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from innovation.models import NEED_TO_REVIEW
from datetime import date


def apply_conference(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ConferenceApplicationForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules passes
            try:
                user = User.objects.get(email=form.cleaned_data['email']) 
            except User.DoesNotExist:
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
            ConferenceApplication.objects.create(date_of_submission=date.today(), 
                                                 year_of_submission=date.today().year,
                                                 applicant=person,
                                                 conference_name=form.cleaned_data['conference_name'],
                                                 conference_dates=form.cleaned_data['conference_dates'],
                                                 conference_city=form.cleaned_data['conference_city'],
                                                 conference_country=form.cleaned_data['conference_country'],
                                                 expected_expenditure=form.cleaned_data['expected_expenditure'],
                                                 paper_title=form.cleaned_data['paper_title'],
                                                 sop=form.cleaned_data['sop'],
                                                 acceptance_email=form.cleaned_data['acceptance_email'],)
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
                user = User.objects.get(email=form.cleaned_data['email']) 
            except User.DoesNotExist:
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