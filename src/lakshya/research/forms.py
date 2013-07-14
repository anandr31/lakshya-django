'''
Created on 14-Jul-2013

@author: srihari
'''

from django import forms
from people.models import DEPARTMENT_CHOICES, COURSE_CHOICES

class ConferenceApplicationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    repeat_email = forms.EmailField()
    roll_num = forms.CharField()
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    year_of_passing = forms.IntegerField()    
    contact_number = forms.CharField()
    conference_name = forms.CharField()
    conference_dates = forms.CharField()
    conference_city = forms.CharField(label="City")
    conference_country = forms.CharField(label="Country")
    expected_expenditure = forms.CharField()    
    paper_title = forms.CharField()
    sop = forms.FileField(label="Statement Of Purpose")
    acceptance_email = forms.FileField()
        
    def clean(self):
        cleaned_data = super(ConferenceApplicationForm, self).clean()
        email = cleaned_data.get('email')
        repeat_email = cleaned_data.get('repeat_email')
        if not email == repeat_email:
            self._errors["repeat_email"] = self.error_class(["You have to enter the same email address"])
        return cleaned_data
    
class InternshipApplicationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    repeat_email = forms.EmailField()
    roll_num = forms.CharField()
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    year_of_passing = forms.IntegerField()    
    contact_number = forms.CharField()
    internship_place = forms.CharField(label="Name of Company/University")
    internship_division = forms.CharField(label="Company Division/ University Department")
    supervisor_name = forms.CharField(required=False)
    internship_dates = forms.CharField()
    internship_city = forms.CharField(label="City")    
    internship_country = forms.CharField(label="Country")
    expected_expenditure = forms.CharField()
    sop = forms.FileField(label="Statement Of Purpose")
        
    def clean(self):
        cleaned_data = super(InternshipApplicationForm, self).clean()
        email = cleaned_data.get('email')
        repeat_email = cleaned_data.get('repeat_email')
        if not email == repeat_email:
            self._errors["repeat_email"] = self.error_class(["You have to enter the same email address"])
        return cleaned_data