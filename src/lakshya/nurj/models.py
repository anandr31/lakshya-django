from django.db import models
from tinymce.models import HTMLField
from nurj.constants import CONTENT_TYPES , CT_ABOUT, CT_GUIDELINES

# Create your models here.
class Content(models.Model):
    """
    Description: Editable Content class, contains static content 
    can be edited from backend. Easier access to admins. 
    """
    type = models.IntegerField(choices=CONTENT_TYPES, null=True, blank=True)
    text = HTMLField(max_length=2000)


