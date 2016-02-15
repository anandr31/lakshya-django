
from datetime import date
from math import floor

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from tinymce import models as tinymce_models

from crowdfunding.utils import IntegerRangeField
from crowdfunding.constants import PROJECT_STATUS, UNAPPROVED, MAIL_NOT_SENT, CAMPAIGN_FULLY_BACKED_MAIL_SENT, \
                                    CAMPAIGN_EXPIRED_UNSUCCESSFULLY_MAIL_SENT, UPDATE_MAIL_NOT_SENT, UPDATE_MAIL_SENT, \
                                    PROJECT_MAIL_STATUSES, UPDATE_MAIL_STATUSES
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)
    description = tinymce_models.HTMLField(max_length=20000)
    author = models.ForeignKey(User)
    goal = IntegerRangeField(default=20000, min_value=20000, max_value=200000)
    period = IntegerRangeField(default=5, min_value=5, max_value=45)
    video_url = models.URLField(max_length=1000, blank=False, default='https://www.youtube.com/watch?v=TRVbrwh4dAQ')
    team = tinymce_models.HTMLField(max_length=10000)
    risks_and_challenges = tinymce_models.HTMLField(max_length=10000, blank=False)
    ordering = models.DecimalField(max_digits=4, decimal_places=1, blank=True)
    start_date = models.DateField(default=date.today)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=UNAPPROVED, choices=PROJECT_STATUS)
    mail_status = models.SmallIntegerField(default=MAIL_NOT_SENT, choices=PROJECT_MAIL_STATUSES)

    def __unicode__(self):
        return str(self.title)

    def save(self, **kwargs):
        if not self.ordering:
            ordering = Project.objects.all().aggregate(
                models.Max('ordering'))['ordering__max']
            if ordering:
                self.ordering = floor(ordering + 1)
            else:
                self.ordering = 1
        super(Project, self).save(**kwargs)

    def get_days_remaining(self):
        remaining = self.period - (date.today() - self.start_date).days
        return remaining if remaining > 0 else 0
    days_remaining = property(get_days_remaining)

    def is_expired(self):
        return self.get_days_remaining() <= 0

    def get_total_pledged_amount(self):
        pledge_amounts = self.pledges.all().values_list('amount', flat=True)
        total = 0
        for amount in pledge_amounts:
            total += amount
        return total
    pledged_amount = property(get_total_pledged_amount)

    def get_percentage_pledged(self):
        if not self.goal:
            return 0
        ratio = float(self.get_total_pledged_amount()) / self.goal
        return int(ratio * 100)
    percentage_pledged = property(get_percentage_pledged)

    def is_fully_pledged(self):
        return self.get_percentage_pledged() >= 100

    def get_total_backers(self):
        return self.pledges.count()
    total_backers = property(get_total_backers)

    def get_image_urls(self):
        images = self.project_image.all().order_by('ordering')
        return [i.image.image for i in images]

    def get_primary_picture_url(self):
        images = self.project_images.all().order_by('ordering')
        return images[0].image.url if images else ''
    primary_picture_url = property(get_primary_picture_url)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_images')
    image = models.ImageField(upload_to='projects/%Y/%m/%d')
    ordering = models.DecimalField(
        default=1, max_digits=4, decimal_places=1, blank=True)

    def __unicode__(self):
        return str(self.project.title)

        def save(self, **kwargs):
            if not self.ordering:
                ordering = ProjectImage.objects.filter(project=self.project)\
                    .aggregate(models.Max('ordering'))['ordering__max']
                if ordering:
                    self.ordering = floor(ordering + 1)
                else:
                    self.ordering = 1
            super(ProjectImage, self).save(**kwargs)

    def show_thumbnail(self):
        return u'<img src="%s" width="100" height="100px"/>' % self.picture.url


class Pledge(models.Model):
    user = models.ForeignKey(User, related_name='pledges')
    amount = models.IntegerField()
    project = models.ForeignKey(Project, related_name='pledges')
    timestamp = models.DateTimeField(auto_now_add=True)
    pledge_fulfilled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.project.title + ' - ' + (self.user.get_full_name() or self.user.username)

class Message(models.Model):
    project = models.ForeignKey(Project, related_name='messages')
    user = models.ForeignKey(User, related_name='messages')
    message = models.TextField(max_length=4000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.title)

class ProjectUpdate(models.Model):
    project = models.ForeignKey(Project, related_name='updates')
    author = models.ForeignKey(User, related_name='project_updates')
    update = tinymce_models.HTMLField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    mail_status = models.SmallIntegerField(default=UPDATE_MAIL_NOT_SENT, choices=UPDATE_MAIL_STATUSES)

    class Meta:
        ordering=('-timestamp',)

    def __unicode__(self):
        return  self.update[:50]
