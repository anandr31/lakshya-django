from django import forms
from django.forms import widgets
from django.forms import ModelForm
from crowdfunding.models import Project,Pledge,ProjectUpdate
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
	
  class Meta:
    model = Project
    exclude = ("author", "status", "ordering", "start_date")

class ProjectUpdateForm(ModelForm):

  class Meta:
	model = ProjectUpdate
	exclude = ("project", "author", "timestamp", "mail_status")
