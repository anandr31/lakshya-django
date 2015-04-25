from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Project(models.Model):
    # Project Status

    UNAPPROVED = 1
    APPROVED = 2
    EXPIRED = 3
    SUCCESSFUL = 4
    CANCELLED = 5

    PROJECT_STATUS = ((UNAPPROVED, 'unapproved'),
                      (APPROVED, 'approved'),
                      (SUCCESSFUL, 'successful'),
                      (CANCELLED, 'cancelled'),
                      )
    title = models.CharField(max_length=60)
    author = models.ForeignKey(User, related_name='ig_projects')
    objective = models.TextField(max_length=500)
    description = HTMLField(max_length=4000)
    team = HTMLField(max_length=1000)
    key_components = HTMLField(max_length=1000)
    team_size = models.IntegerField()
    start_date = models.DateField()
    status = models.SmallIntegerField(
        default=UNAPPROVED, choices=PROJECT_STATUS)

    def __unicode__(self):
        return str(self.title)

    def get_image_urls(self):
        images = self.project_image.all().order_by('ordering')
        return [i.image.image for i in images]

    def get_primary_picture_url(self):
        images = self.project_image.all().order_by('ordering')
        return images[0].image.url if images else ''
#       primary_picture_url = property(get_primary_picture_url)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_image')
    image = models.ImageField(upload_to='projects')
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


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='igsponsors/')
    website = models.URLField()
    description = models.TextField(max_length=2000)
