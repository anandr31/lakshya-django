from django import forms
from django.forms import widgets
from django.forms import ModelForm
from crowdfunding.models import Project,Pledge
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
	
  class Meta:
    model = Project
    exclude = ("author", "status", "ordering", "start_date")
