from django import forms
from models import *

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields =['mobile','team','problem']

    def clean(self):
        return super(RegistrationForm, self).clean()

class RegForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control '}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'form-control '}))
    mobile = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control '}))
    problem = forms.ModelChoiceField(queryset=ProblemStatement.objects.all().filter(is_active=True), required=True,widget=forms.Select(attrs={'class' : 'form-control '}))
    team = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control ' }))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,required=True,widget=forms.Select(attrs={'class' : 'form-control '}))
    tee = forms.ChoiceField(choices=TEE_CHOICES,required=True,widget=forms.Select(attrs={'class' : 'form-control '}))
    roll_no = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control '}))
    year = forms.ChoiceField(choices=YEAR_CHOICES,required=True,widget=forms.Select(attrs={'class' : 'form-control '}))
    course = forms.ChoiceField(choices=COURSE_CHOICES,required=True,widget=forms.Select(attrs={'class' : 'form-control '}))
    branch = forms.ChoiceField(choices=BRANCH_CHOICES,required=True,widget=forms.Select(attrs={'class' : 'form-control '}))
    mess = forms.ChoiceField(choices=MESS_CHOICES,required=True,widget=forms.Select(attrs={'class' : 'form-control '}))

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile) != 10:
            raise forms.ValidationError("The mobile number must be 10 digits")
        return mobile
