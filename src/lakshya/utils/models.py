from django.db import models
from people.models import Person

# Create your models here.
class LakshyaUpdate(models.Model):
    update_text = models.TextField(null=True, blank=True)
    photo = models.ImageField("Update photo", upload_to="update_pics/", null=True, blank=True)
    date_of_entry = models.DateField(null=True, blank=True,)
    sorting = models.IntegerField()
    active = models.BooleanField()
    
class LakskhyaTestimonial(models.Model):
    testimonial_text = models.TextField(null=True, blank=True)
    person = models.ForeignKey(Person, )
    designation = models.CharField(max_length = 50)
    date_of_entry = models.DateField(null=True, blank=True, auto_now=True)
    sorting = models.IntegerField()
    active = models.BooleanField()    