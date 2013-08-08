'''
Created on 08-Aug-2013

@author: srihari
'''
from django.forms import ModelForm
from models import Registration
from django import forms


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
    