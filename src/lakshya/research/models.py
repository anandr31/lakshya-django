from django.db import models
from people.models import Person, DEPARTMENT_CHOICES
from accounts.models import Expense
from innovation.models import APPLICATION_STATUS, NEED_TO_REVIEW


class ConferenceApplication(models.Model):
    date_of_submission = models.DateTimeField()
    year_of_submission = models.IntegerField()
    
    applicant = models.ForeignKey(Person)
    
    conference_name = models.CharField(max_length=50)
    conference_dates = models.CharField(max_length=50)
    conference_city = models.CharField(max_length=50)
    conference_country = models.CharField(max_length=50)
    conference_url = models.CharField(max_length=100, null=True, blank=True)
    expected_expenditure = models.CharField(max_length=15)
 
    paper_title = models.CharField(max_length=200)
    sop = models.FileField(upload_to="conference_sop", null=True, blank=True)
    acceptance_email = models.FileField(upload_to="conference_email", null=True, blank=True, 
                                        help_text="PFD of Acceptance and Review Email")
    research_paper = models.FileField(upload_to="conference_paper", null=True, blank=True)    
    review = models.TextField(blank=True)
    status = models.IntegerField(choices=APPLICATION_STATUS, default=NEED_TO_REVIEW)
 
    def __unicode__(self):
        return self.paper_title

    def get_applicant_detail(self):
        retval = self.applicant.name() + "<br>" + self.applicant.get_course_display() + "," \
                + self.applicant.get_department_display() \
              + "," + str(self.applicant.year_of_passing) + "<br>" + self.applicant.email() + "<br>" \
              + self.applicant.contact_number + "<br>" + \
              "<a href='/admin/people/person/%d'>More Details</a>"%(self.applicant.id)        
        return retval
    
    get_applicant_detail.allow_tags = True
    get_applicant_detail.short_description = "Applicant Details"    
    
    
class InternshipApplication(models.Model):
    date_of_submission = models.DateTimeField()
    year_of_submission = models.IntegerField()
    
    applicant = models.ForeignKey(Person)
    
    internship_place = models.CharField("Company/University", max_length=50)
    internship_division = models.CharField(max_length=50, null=True, blank=True)
    supervisor_name = models.CharField(max_length=50, null=True, blank=True)
    internship_dates = models.CharField(max_length=50)
    internship_city = models.CharField(max_length=50)
    internship_country = models.CharField(max_length=50)
    expected_expenditure = models.CharField(max_length=15)
    sop = models.FileField(upload_to="conference_sop", null=True, blank=True)

    review = models.TextField(blank=True)
    status = models.IntegerField(choices=APPLICATION_STATUS, default=NEED_TO_REVIEW)
 
    def __unicode__(self):
        return self.internship_place

    def get_applicant_detail(self):
        retval = self.applicant.name() + "<br>" + self.applicant.get_course_display() + "," \
                + self.applicant.get_department_display() \
              + "," + str(self.applicant.year_of_passing) + "<br>" + self.applicant.email() + "<br>" \
              + self.applicant.contact_number + "<br>" + \
              "<a href='/admin/people/person/%d'>More Details</a>"%(self.applicant.id)        
        return retval
    
    get_applicant_detail.allow_tags = True
    get_applicant_detail.short_description = "Applicant Details"    
    
    
class Panelist(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,)
    branch = models.IntegerField(choices=DEPARTMENT_CHOICES)
    other_info = models.TextField(null=True, blank=True)
    active = models.BooleanField("Is he/she actively involved", default=False,)
    
    def __unicode__(self): 
        return self.name    


class ConferenceApplicationFeedback(models.Model):
    application = models.ForeignKey(ConferenceApplication)
    panelist = models.ForeignKey(Panelist)
    conference_quality = models.IntegerField(choices=[(i,i) for i in range(0,6)])
    paper_quality = models.IntegerField(choices=[(i,i) for i in range(0,6)])
    significance_of_contribution = models.IntegerField(choices=[(i,i) for i in range(0,6)])
    originality_of_content = models.IntegerField(choices=[(i,i) for i in range(0,6)])
    technical_quality = models.IntegerField(choices=[(i,i) for i in range(0,6)])
    recommended_extent_of_funding = models.IntegerField(choices=[(i,i) for i in range(0,6)])
    feedback = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.application.paper_title