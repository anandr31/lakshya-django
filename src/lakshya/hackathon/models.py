from django.db import models

YEAR_CHOICES = ((1, "First"),
                (2, "Second"),
                (3, "Third"),
                (4, "Final"),
)

COURSE_CHOICES = ((1, "B.Tech"),
                  (2, "M.Tech"),
                  (3, "MCA"),
                  (4, "MSc"),
                  (5, "MBA"),
                  (6, "PhD"),
)

BRANCH_CHOICES = ((1, "Civil"),
                  (2, "Electrical"),
                  (3, "Electronics & Communication"),
                  (4, "Mechanical"),
                  (5, "Metallurgical & Materials"),
                  (6, "Chemical"),
                  (7, "Computer Science"),
                  (8, "Biotechnology"),
                  (9, "Physics"),
                  (10, "Chemistry"),
                  (11, "School of Management"),
)

MESS_CHOICES = ((1, "First"),
                (2, "Second"),
                (3, "Third"),
                (4, "Fourth"),
                (5, "Fifth"),
                (6, "IFC-A"),
                (7, "IFC-B"),
                (8, "LH"),
)

TEE_CHOICES = ((1, "S"),
               (2, "M"),
               (3, "L"),
               (4, "XL"),
               (5, "XXL"),
)

GENDER_CHOICES = ((1, "MALE"),
                  (2, "FEMALE"),
)


class ProblemStatement(models.Model):
    hackathon = models.ForeignKey('Hackathon', null=True)
    name = models.CharField("Problem", max_length=100, blank=False)
    add_link = models.URLField("Additional Link", max_length=500, blank=False, null=True)
    is_active = models.BooleanField("Activated", default=True)

    def __unicode__(self):
        return  self.name


class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    banner = models.ImageField(upload_to='hackathon_banners', blank=True)
    report = models.FileField("Report (PDF)", upload_to='hackathon_reports', blank=True)
    facebook_event_code = models.CharField(max_length=255, blank=True)
    pictures_link = models.CharField(max_length=1000, blank=True)
    venue = models.CharField("Venue", max_length=200, blank=True)
    is_active = models.BooleanField("Active", default=True)

    def __unicode__(self):
        return self.name


class Participant(models.Model):
    hackathon = models.ForeignKey(Hackathon, null=True)
    name = models.CharField("Name", max_length=50, blank=False)
    roll_no = models.CharField("Roll Number", max_length=15, blank=False, default=0)
    year = models.SmallIntegerField("Year", choices=YEAR_CHOICES, default=1)
    course = models.SmallIntegerField("Course", choices=COURSE_CHOICES, default=1)
    branch = models.SmallIntegerField("Branch", choices=BRANCH_CHOICES, default=1)
    mess = models.SmallIntegerField("Mess", choices=MESS_CHOICES, default=1)
    email = models.EmailField("Email", blank=False)
    mobile = models.CharField("Mobile", blank=False, max_length=10)
    problem = models.ForeignKey(ProblemStatement)
    team = models.CharField("Team", max_length=100, blank=False)
    tee_shirt_size = models.SmallIntegerField("Tee Size", choices=TEE_CHOICES, default=1)
    gender = models.SmallIntegerField("Gender", choices=GENDER_CHOICES, default=1)

    def __unicode__(self):
        return  self.name

    def get_index(self, x):
        return int(x) - 1

    def YEAR(self):
        index = self.get_index(self.year)
        return YEAR_CHOICES[index][1]

    def MESS(self):
        index = self.get_index(self.mess)
        return MESS_CHOICES[index][1]

    def COURSE(self):
        index = self.get_index(self.course)
        return COURSE_CHOICES[index][1]

    def BRANCH(self):
        index = self.get_index(self.branch)
        return BRANCH_CHOICES[index][1]

    def GENDER(self):
        index = self.get_index(self.gender)
        return GENDER_CHOICES[index][1]


class Sponsors(models.Model):
    name = models.CharField("Name", max_length=255)
    desc = models.TextField("Description", max_length=5000, blank=True, null=True)
    url = models.URLField("Company URL", blank=True)
    image = models.ImageField("Company Logo", blank=True, null=True, upload_to='hackathon_sponsors')
    hackathon = models.ForeignKey(Hackathon, null=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    SPONSOR = 1
    MENTOR = 2
    OTHER = 3
    TYPES = ((SPONSOR, "Sponsor"),
             (MENTOR, "Mentor"),
             (OTHER, "Other"))

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    contact_info = models.CharField(max_length=255)
    type = models.SmallIntegerField(choices=TYPES, default=OTHER)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Mentor(models.Model):
    hackathon = models.ForeignKey(Hackathon, null=True)
    name = models.CharField(max_length=255)
    picture = models.ImageField(max_length=1000, upload_to='hackathon_mentors', blank=True, null=True)
    linkedin_profile = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=5000, blank=True)

    def __unicode__(self):
        return self.name
