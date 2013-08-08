from django.db import models

ALUMNI = 0
STUDENT = 1
PROFILE_TYPE = ((ALUMNI, "Rs 1,500 ( For Alumni )"),
                (STUDENT, "Rs 500 ( For Students )"),)

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    batch = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    amount  = models.IntegerField(choices=PROFILE_TYPE, default=ALUMNI)
    
    def __unicode__(self):
        return str(self.name)