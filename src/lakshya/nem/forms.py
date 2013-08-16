'''
Created on 08-Aug-2013

@author: srihari
'''
from models import PROFILE_TYPE
from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField()
    batch = forms.CharField()
    branch = forms.CharField()
    email = forms.EmailField()
    amount = forms.ChoiceField(choices=PROFILE_TYPE)

    