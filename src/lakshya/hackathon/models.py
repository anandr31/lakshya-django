from django.db import models

# Create your models here.
class ProblemStatement(models.Model):
    name = models.CharField("Problem",max_length=100,blank=False)

    def __unicode__(self):
        return  self.name;
    
class Participant(models.Model):
    name = models.CharField("Name",max_length=50,blank=False)
    email = models.EmailField("Email",blank=False)
    mobile = models.IntegerField("Mobile Number",max_length=10,blank=False)
    problem = models.OneToOneField(ProblemStatement)
    team = models.CharField("Team",max_length=100,blank=False)

    def __unicode__(self):
        return  self.name;

