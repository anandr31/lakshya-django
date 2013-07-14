# Create your views here.
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms import IspApplicationForm
from django.contrib.auth.models import User
from people.models import Person
from datetime import date
from innovation.models import IspApplication, NEED_TO_REVIEW
from django.http import HttpResponse

def get_innovation_list(request, project_name):
    if not project_name:
        project_name = "hovamarine"
    return render_to_response("innovations_list.html", 
                              RequestContext(request, {'project_name':project_name}))
    
def apply_innovation(request):
    if request.method == 'POST': # If the form has been submitted...
        form = IspApplicationForm(request.POST, request.FILES) # A form bound to the POST data
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
            IspApplication.objects.create(date_of_submission=date.today(), year_of_submission=
                                                          date.today().year, abstract=form.cleaned_data['abstract'],
                                                          title=form.cleaned_data['title_of_project'],
                                                          status=NEED_TO_REVIEW, member=person, 
                                                          other_member_details=form.cleaned_data['other_member_details'])            
            return render_to_response("apply_innovation_success.html", RequestContext(request, {}))
    else:
        form = IspApplicationForm() # An unbound form

    return render(request, 'apply_innovation.html', {
        'form': form,
    })
