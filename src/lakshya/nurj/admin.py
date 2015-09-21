from django.contrib import admin
from nurj.models import Content, Applicant

# Register your models here.
# admin.autodiscover()

admin.site.register(Content)
admin.site.register(Applicant)