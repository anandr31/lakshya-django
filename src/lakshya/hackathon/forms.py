from django import forms
from models import *

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields =['name','email','mobile','team','problem']

    def clean(self):
        return super(RegistrationForm, self).clean()

class RegForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control input-hg'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'form-control input-hg'}))
    mobile = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control input-hg'}))
    team = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control input-hg' }))
    problem = forms.ModelChoiceField(queryset=ProblemStatement.objects.all(), required=True)

