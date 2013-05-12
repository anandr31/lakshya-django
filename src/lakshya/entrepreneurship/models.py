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

class Company(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=140, null=True, blank=True)
    sectors = models.ManyToManyField(Sector, blank=True)
    founders = models.ManyToManyField(Person, through='FounderDetail') 
    website_url = models.URLField(max_length=100, null=True, blank=True)
    video_url = models.URLField(max_length=100, null=True, blank=True)
    logo = models.FileField("Update photo", upload_to="team_pics/", null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"

class FounderDetail(models.Model):
    company = models.ForeignKey(Company)
    person = models.ForeignKey(Person)
    bio = models.CharField(max_length=140, null=True, blank=True)
    designation = models.CharField("Designation", max_length=50, null=True, blank=True)
    photo = models.FileField("Update photo", upload_to="team_pics/", null=True, blank=True)
    fb_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    blog_link = models.URLField(null=True, blank=True)
    