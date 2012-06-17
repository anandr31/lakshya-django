from django.db import models
from datetime import datetime

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
    description = models.TextField(help_text="What it is about, what problem you are trying to solve etc")
    abstract = models.FileField(upload_to="innovation_abstracts", blank=True)
    team_members = models.ManyToManyField(Person)
    reviewer = models.ForeignKey(Person, related_name="reviewer")
    review = models.TextField(blank=True)
    status = models.IntegerField(choices=INNOVATION_APPLICATION_STATUS, default=NEED_TO_REVIEW)

    
class Innovation(models.Model):
    application = models.ForeignKey(InnovationApplication)
    guide = models.ForeignKey(Person)


class InnovationUpdate(models.Model):
    innovation = models.ForeignKey(Innovation)
    date_of_update = models.DateField(null=True, blank=True, auto_now_add=True)
    update = models.TextField()

    
class InnovationUpdateImage(models.Model):
    innovation_update = models.ForeignKey(InnovationUpdate, related_name="images")
    image = models.ImageField(upload_to="innovation_update_images")
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
    