from django.db import models
from django.contrib.auth.models import User

BTECH = 0
MTECH = 1
PHD = 2
COURSE_CHOICES = ((BTECH, "B.Tech"),
                  (MTECH, "M.Tech"),
                  (PHD, "Phd"))

ECE = 0
EEE = 1
CSE = 2
MECH = 3
CIVIL = 4
CHEM = 5
METALLURGY = 6
BIOTECH = 7
DEPARTMENT_CHOICES = ((ECE, "ECE"),
                      (EEE, "EEE"),
                      (CSE, "CSE"),
                      (MECH, "MECH"),       
                      (CIVIL, "CIVIL"),
                      (CHEM, "CHEM"),
                      (METALLURGY, "METALLURGY"),
                      (BIOTECH, "BIOTECH"),)

class Person(models.Model):
    user = models.OneToOneField(User)
    #Address
    billing_address = models.TextField("Billing Address", blank=True)
    billing_landmark = models.CharField("Landmark", max_length=100, blank=True)
    billing_city = models.CharField("City", max_length=50, blank=True)
    billing_state = models.CharField("State", max_length=50, blank=True)
    billing_postal_code = models.CharField("Pin Code", max_length=30, blank=True)
    billing_country = models.CharField("Country", max_length=50, blank=True)
    contact_number = models.CharField("Phone Number", max_length = 20, blank=True)
    pan_number = models.CharField("PAN Number", max_length = 20, blank=True)
        
    #if NITW
    is_nitw_alumni = models.BooleanField(blank=True)
    course = models.IntegerField(choices=COURSE_CHOICES, default=BTECH, blank=True, null=True)
    department = models.IntegerField(choices=DEPARTMENT_CHOICES, blank=True, null=True)
    year_of_passing = models.IntegerField(blank=True, null=True)
    profile_pic = models.FileField("Update photo", upload_to="profile_pics/", null=True, blank=True)
    
    
    def __unicode__(self):
        return self.user.first_name
    
    def name(self):
        return self.user.first_name + " " + self.user.last_name
    
    def get_full_address(self):
        return self.billing_address + ", Landmark: " + self.billing_landmark + ", " + self.billing_city + "- " + self.billing_postal_code + ", " + \
            self.billing_state + ", " + self.billing_country


class Person_preference(models.Model):
    person = models.OneToOneField(Person)
    is_subscribed_for_newsletter = models.BooleanField(default=True, blank=False)
    show_donations = models.BooleanField(default=True, blank=True)
    
 
class TeamMember(models.Model):
    name = models.CharField("Full Name", max_length=100,)
    slug = models.CharField("Slug", max_length=100,)
    designation = models.CharField("Designation", max_length=100,)
    photo = models.FileField("Update photo", upload_to="team_pics/", null=True, blank=True)
    description = models.TextField("Description",)
    fb_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    blog_link = models.URLField(null=True, blank=True)

    
    