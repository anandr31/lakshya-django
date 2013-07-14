
'''
Created on 13-Jul-2013

@author: srihari
'''


from django import forms
from people.models import DEPARTMENT_CHOICES, COURSE_CHOICES

class IspApplicationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    repeat_email = forms.EmailField()
    roll_num = forms.CharField()
    course = forms.ChoiceField(choices=COURSE_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    year_of_passing = forms.IntegerField()    
    contact_number = forms.CharField()
    other_member_details = forms.CharField(required=False)
    title_of_project = forms.CharField()
    expected_expenditure = forms.CharField()
    abstract = forms.FileField()
        
    def clean(self):
        cleaned_data = super(IspApplicationForm, self).clean()
        email = cleaned_data.get('email')
        repeat_email = cleaned_data.get('repeat_email')
        if not email == repeat_email:
            self._errors["repeat_email"] = self.error_class(["You have to enter the same email address"])
        return cleaned_data