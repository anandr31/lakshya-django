from django.db import models

from people.models import Person
from accounts.models import Expense

NEED_TO_REVIEW = 0
REVIEWED = 1
ACCEPTED = 4
REJECTED = 5
INNOVATION_APPLICATION_STATUS = ((NEED_TO_REVIEW, "Need to review"),
                                 (REVIEWED, "Reviewed"),
                                 (ACCEPTED, "Accepted"),
                                 (REJECTED, "Rejected"))
class InnovationApplication(models.Model):
    date_of_submission = models.DateTimeField()
    year_of_submission = models.IntegerField()
    
    title = models.CharField(max_length=200)
    abstract = models.FileField(upload_to="innovation_abstracts", null=True, blank=True)
    expected_expenditure = models.CharField(max_length=15)
    team_member = models.ForeignKey(Person, null=True, blank=True)
    other_member_details = models.TextField(help_text="Enter your team member details")
    reviewer = models.ForeignKey(Person, related_name="reviewer", null=True, blank=True)
    review = models.TextField(blank=True)
    status = models.IntegerField(choices=INNOVATION_APPLICATION_STATUS, default=NEED_TO_REVIEW)
    
    def __unicode__(self):
        return self.title
    
    def get_team_member_detail(self):
        retval = self.team_member.name() + "<br>" + self.team_member.get_course_display() + "," \
                + self.team_member.get_department_display() \
              + "," + str(self.team_member.year_of_passing) + "<br>" + self.team_member.email() + "<br>" \
              + self.team_member.contact_number + "<br>" + \
              "<a href='/admin/people/person/%d'>More Details</a>"%(self.team_member.id)        
        return retval
    
    get_team_member_detail.allow_tags = True
    get_team_member_detail.short_description = "Team Member Details"
    
class Innovation(models.Model):
    application = models.OneToOneField(InnovationApplication)
    guide = models.ForeignKey(Person)
    
        
    def get_title(self):
            return self.application.title
    get_title.short_description = "Title"
    
    def get_year_of_submission(self):
            return self.application.year_of_submission
    get_year_of_submission.short_description = "Year of submission"
    
    def __unicode__(self):
        return self.application.title


class InnovationUpdate(models.Model):
    innovation = models.ForeignKey(Innovation)
    date_of_update = models.DateField(null=True, blank=True,)
    update = models.TextField()
    
    def get_link(self):
        if self.id:
            return "<a href='/admin/innovation/innovationupdate/%d'>%d</a>" % (self.id, self.id)
        else:
            return ""
    get_link.allow_tags = True
    
class InnovationUpdateImage(models.Model):
    innovation_update = models.ForeignKey(InnovationUpdate, related_name="images")
    image = models.FileField(upload_to="innovation_update_images")
    caption = models.CharField(max_length=100, blank=True)
    sort_order = models.IntegerField(default=0)


class InnovationUpdateVideo(models.Model):
    innovation_update = models.ForeignKey(InnovationUpdate, related_name="videos")
    video = models.FileField(upload_to="innovation_update_videos")
    caption = models.CharField(max_length=100, blank=True)
    sort_order = models.IntegerField(default=0)    

    
class InnovationPayment(models.Model):
    innovation = models.ForeignKey(Innovation)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense = models.ForeignKey(Expense)
    
    def __unicode__(self):
        return str(self.innovation) + " : Rs " + str(self.amount) +  " : " +str(self.expense.date_of_expense)    
    
    def save(self, **kwargs):
        if not self.id:
            self.amount = self.expense.amount
        super(InnovationPayment, self).save(**kwargs)
        
    