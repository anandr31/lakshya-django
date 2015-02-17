from django.db import models

from people.models import Person
from accounts.models import Expense

NEED_TO_REVIEW = 0
REVIEWED = 1
ACCEPTED = 4
REJECTED = 5
APPLICATION_STATUS = ((NEED_TO_REVIEW, "Need to review"),
                                 (REVIEWED, "Reviewed"),
                                 (ACCEPTED, "Accepted"),
                                 (REJECTED, "Rejected"))


class IspApplication(models.Model):
    date_of_submission = models.DateTimeField()
    year_of_submission = models.IntegerField()

    title = models.CharField(max_length=200)
    abstract = models.FileField(upload_to="innovation_abstracts", null=True, blank=True)
    expected_expenditure = models.CharField(max_length=15)
    member = models.ForeignKey(Person)
    other_member_details = models.TextField(help_text="Enter your team member details")
    review = models.TextField(blank=True)
    status = models.IntegerField(choices=APPLICATION_STATUS, default=NEED_TO_REVIEW)

    def __unicode__(self):
        return self.title

    def get_member_detail(self):
        retval = self.member.name() + "<br>" + self.member.get_course_display() + "," \
                + self.member.get_department_display() \
              + "," + str(self.member.year_of_passing) + "<br>" + self.member.email() + "<br>" \
              + self.member.contact_number + "<br>" + \
              "<a href='/admin/people/person/%d'>More Details</a>" % (self.member.id)
        return retval

    get_member_detail.allow_tags = True
    get_member_detail.short_description = "Team Member Details"


class Innovation(models.Model):
    application = models.OneToOneField(IspApplication)
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
        return str(self.innovation) + " : Rs " + str(self.amount) + " : " + str(self.expense.date_of_expense)

    def save(self, **kwargs):
        if not self.id:
            self.amount = self.expense.amount
        super(InnovationPayment, self).save(**kwargs)


class InnovationInstrument(models.Model):
    """An instrument used in the innovation garage"""
    HAVE = 1
    NEEDED = 2
    STATUSES = ((HAVE, "Have"),
                (NEEDED, "Needed"))

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=140)
    image = models.ImageField("Picture", max_length=1000, upload_to='innovation_instruments')
    status = models.SmallIntegerField(choices=STATUSES, default=NEEDED)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.name
