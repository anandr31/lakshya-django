from django.forms import ModelForm
from nurj.models import Applicant

class ApplicationForm(ModelForm):
	class Meta:
		model = Applicant