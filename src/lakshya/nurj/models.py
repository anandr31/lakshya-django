from django.db import models
from tinymce.models import HTMLField
from lakshya import settings
from nurj.constants import CONTENT_TYPES , CT_ABOUT, CT_GUIDELINES, COURSES, BRANCHES, CIVIL, ST_ARTICLE, SUB_TYPES

# Create your models here.
class Content(models.Model):
    """
    Description: Editable Content class, contains static content 
    can be edited from backend. Easier access to admins. 
    """
    type = models.IntegerField(choices=CONTENT_TYPES, null=True, blank=True)
    text = HTMLField(max_length=2000)


def get_upload_path(suffix):
    def wrapper(self, filename):
        return settings.MEDIA_ROOT + "/" + suffix + "/" + self.name + "/" + filename
    return wrapper


class Applicant(models.Model):
    """
    Description: Applicant model , contains all the information 
    including the urls of the files uploaded.
    """
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True)
    course = models.IntegerField(choices=COURSES, default=1)
    branch = models.IntegerField(choices=BRANCHES, default=CIVIL)
    rollno = models.CharField(max_length=255, null=True, blank=True)
    submission_type = models.IntegerField(choices=SUB_TYPES, default=ST_ARTICLE)
    title = models.CharField(max_length=100,null=True,blank=True)
    title_page = models.FileField(upload_to=get_upload_path('title_pages'))
    blinded_script = models.FileField(upload_to=get_upload_path('manuscripts'))




