from django.db import models

YEAR_CHOICES = ((1,"First"),
                (2,"Second"),
                (3,"Third"),
                (4,"Final"),
)

COURSE_CHOICES = ((1,"B.Tech"),
                  (2,"M.Tech"),
                  (3,"MCA"),
                  (4,"MSc"),
                  (5,"MBA"),
                  (6,"PhD"),
)

BRANCH_CHOICES = ((1,"Civil"),
                  (2,"Electrical"),
                  (3,"Electronics & Communication"),
                  (4,"Mechanical"),
                  (5,"Metallurgical & Materials"),
                  (6,"Chemical"),
                  (7,"Computer Science"),
                  (8,"Biotechnology"),
                  (9,"Physics"),
                  (10,"Chemistry"),
                  (11,"School of Management"),
)

MESS_CHOICES = ((1,"First"),
                (2,"Second"),
                (3,"Third"),
                (4,"Fourth"),
                (5,"Fifth"),
                (6,"IFC-A"),
                (7,"IFC-B"),
                (8,"LH"),
)

TEE_CHOICES = ((1,"S"),
               (2,"M"),
               (3,"L"),
               (4,"XL"),
               (5,"XXL"),
)

GENDER_CHOICES = ((1,"MALE"),
                  (2,"FEMALE"),
)

def get_index(x):
    return int(x) - 1

class ProblemStatement(models.Model):
    name = models.CharField("Problem",max_length=100,blank=False)
    add_link = models.URLField("Additional Link",max_length=500,blank=False,null=True)

    def __unicode__(self):
        return  self.name

class Participant(models.Model):
    name = models.CharField("Name",max_length=50,blank=False)
    roll_no = models.CharField("Roll Number",max_length=15,blank=False,default=0)
    year = models.CharField("Year",choices=YEAR_CHOICES,default=1,max_length=50)
    course = models.CharField("Course",choices=COURSE_CHOICES,default=1,max_length=50)
    branch = models.CharField("Branch",choices=BRANCH_CHOICES,default=1,max_length=50)
    mess = models.CharField("Mess",choices=MESS_CHOICES,default=1,max_length=50)
    email = models.EmailField("Email",blank=False)
    mobile = models.CharField("Mobile",blank=False,max_length=10)
    problem = models.ForeignKey(ProblemStatement)
    team = models.CharField("Team",max_length=100,blank=False)
    tee_shirt_size = models.CharField("Tee Size",choices=TEE_CHOICES,default=1,max_length=50)
    gender = models.CharField("Gender",choices=GENDER_CHOICES,default=1,max_length=50)

    def __unicode__(self):
        return  self.name

    def YEAR(self):
        index = get_index(self.year)
        return YEAR_CHOICES[index][1]

    def MESS(self):
        index = get_index(self.mess)
        return MESS_CHOICES[index][1]

    def COURSE(self):
        index = get_index(self.course)
        return COURSE_CHOICES[index][1]

    def BRANCH(self):
        index = get_index(self.branch)
        return BRANCH_CHOICES[index][1]

    def GENDER(self):
        index = get_index(self.gender)
        return GENDER_CHOICES[index][1]

