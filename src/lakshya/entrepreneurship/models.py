from django.db import models
from people.models import Person

class Sector(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.CharField(max_length=140, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def count(self):
        return Company.objects.filter(sectors=self).count()
    
class AttributeOption(models.Model):
    """
    Allows arbitrary name/value pairs to be attached to a Company.
    By defining the list, the user will be presented with a predefined
    list of attributes instead of a free form field.
    The validation field should contain a regular expression that can be
    used to validate the structure of the input.
    Possible usage : Number of employees, Founding Year etc
    """    
    name = models.CharField(max_length = 100)
    slug = slug = models.SlugField(max_length = 100, blank=True)
    ordering = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, blank=True)
    description = models.TextField(null=True, blank=True)
    sectors = models.ManyToManyField(Sector, blank=True)
    founders = models.ManyToManyField(Person, through='FounderDetail') 
    website_url = models.URLField(max_length=100, null=True, blank=True)
    video_url = models.URLField("Video Url", max_length=100, null=True, blank=True)
    logo = models.FileField("Company Logo", upload_to="company/logo/", null=True, blank=True)
    
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    postal_code = models.CharField("Pin Code", max_length=30, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    contact_number = models.CharField("Phone Number", max_length = 20, blank=True)
    contact_email = models.EmailField("Email Id", max_length = 40, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"
        
class CompanyAttribute(models.Model):
    """
    Allows arbitrary name/value pairs (as strings) to be attached to a company.
    This is a simple way to add extra text or numeric info to a company.
    """
    company = models.ForeignKey(Company)
    option = models.ForeignKey(AttributeOption)
    value = models.CharField(max_length=255, null=True, blank=True)
    
class CompanyPhoto(models.Model):
    company = models.ForeignKey(Company)
    photo = models.FileField("Update photo", upload_to="company/pics/", null=True, blank=True)
    caption = models.CharField("Caption", max_length=50, null=True, blank=True)
    
class FounderDetail(models.Model):
    company = models.ForeignKey(Company)
    person = models.ForeignKey(Person)
    designation = models.CharField("Designation", max_length=50, null=True, blank=True)
    photo = models.FileField("Update photo", upload_to="team_pics/", null=True, blank=True)
    fb_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    blog_link = models.URLField(null=True, blank=True)
    
    

    

    