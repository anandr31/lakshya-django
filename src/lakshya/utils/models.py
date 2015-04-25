from django.db import models
from people.models import Person
from tinymce.models import HTMLField

# Create your models here.
class LakshyaUpdate(models.Model):
    update_text = models.TextField(null=True, blank=True)
    photo = models.FileField("Update photo", upload_to="update_pics/", null=True, blank=True)
    date_of_entry = models.DateField(null=True, blank=True,)
    sorting = models.IntegerField()
    active = models.BooleanField()
    
class LakshyaTestimonial(models.Model):
    testimonial_text = models.TextField(null=True, blank=True)
    photo = models.FileField("Update photo", upload_to="update_pics/", null=True, blank=True)
    video_link = models.TextField(null=True, blank=True)
    person = models.ForeignKey(Person, )
    designation = models.CharField(max_length = 50)
    date_of_entry = models.DateField(null=True, blank=True, auto_now=True)
    sorting = models.IntegerField()
    active = models.BooleanField()

class Contact(models.Model):
    PC_IGARAGE = 1
    PC_HACKATHON = 2
    PC_CROWDFUNDING = 3
    PC_OTHERS = 4
    PROJECT_CHOICES = ((PC_IGARAGE, "Innovation Garage"),
                       (PC_HACKATHON, "Hackaton"),
                       (PC_CROWDFUNDING, "Crowdfunding"),
                       (PC_OTHERS, "Others"))
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email_or_phone = models.CharField(max_length=255)
    project = models.SmallIntegerField(choices=PROJECT_CHOICES,default=PC_OTHERS)
    message = models.TextField()

    def __unicode__(self):
        return self.name + ' from ' + self.company


class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/')
    description = HTMLField(max_length=4000)
    priority = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name
