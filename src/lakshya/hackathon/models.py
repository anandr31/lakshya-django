from django.db import models

# Create your models here.
class ProblemStatement(models.Model):
    name = models.CharField("Problem",max_length=100,blank=False)

    def __unicode__(self):
        return  self.name

class Participant(models.Model):
    name = models.CharField("Name",max_length=50,blank=False)
    email = models.EmailField("Email",blank=False)
    mobile = models.CharField("Mobile",blank=False,max_length=10)
    problem = models.ForeignKey(ProblemStatement)
    team = models.CharField("Team",max_length=100,blank=False)

    def __unicode__(self):
        return  self.name

