from django.db import models
from people.models import Person
from accounts.models import DonationFund, Expense, TRANSACTION_CHOICES
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.models import User

YET_TO_SHORTLIST = 0
NEED_TO_VERIFY = 1
VERIFIED = 3
ACCEPTED = 4
REJECTED = 5
SCHOLARSHIP_APPLICATION_STATUS = ((YET_TO_SHORTLIST, "Yet to shortlist"),
                                  (NEED_TO_VERIFY, "Need to verify"),
                                  (VERIFIED, "Verified"),
                                  (ACCEPTED, "Accepted"),
                                  (REJECTED, "Rejected"))

FIRST_SEMESTER = 1
SECOND_SEMESTER = 2
THIRD_SEMESTER = 3
FOURTH_SEMESTER = 4
FIFTH_SEMESTER = 5
SIXTH_SEMESTER = 6
SEVENTH_SEMESTER = 7
EIGHT_SEMESTER = 8
SEMESTER_CHOICES = ((FIRST_SEMESTER, "First Semester"),
                    (SECOND_SEMESTER, "Second Semester"),
                    (THIRD_SEMESTER, "Third Semester"),
                    (FOURTH_SEMESTER, "Fourth Semester"),
                    (FIFTH_SEMESTER, "Fifth Semester"),
                    (SIXTH_SEMESTER, "Sixth Semster"),
                    (SEVENTH_SEMESTER, "Seventh Semster"),
                    (EIGHT_SEMESTER, "Eighth Semster"),
                    )

TUTION_FEES = 1
HOSTEL_FEES = 2
MESS_FEES = 3
OTHERS = 4
SCHOLARSHIP_PAYMENT_REASON = ((TUTION_FEES, "Tution fees"),
                              (HOSTEL_FEES, "Hostel fees"),
                              (MESS_FEES, "Mess fees"),
                              (OTHERS, "Others"),
                              )


GRADE_CHOICES = (("Ex", "Ex"),
                 ("A", "A"),
                 ("B", "B"),
                 ("C", "C"),
                 ("D", "D"),
                 ("P", "P"),
                 ("F", "F"),
                 )


MALE = 0
FEMALE = 1
SEX_CHOICES = ((MALE, "Male"),
               (FEMALE, "Female"),
               )

SSC_CBSE = 0
SSC_STATE = 1
SSC_BOARD_CHOICES = ((SSC_CBSE, "Central Board - CBSE"),
                     (SSC_STATE, "State Board"),
                     )

INTERMEDIATE_CBSE = 0
INTERMEDIATE_STATE = 1
INTERMEDIATE_BOARD_CHOICES = ((INTERMEDIATE_CBSE, "Central Board - CBSE"),
                     (INTERMEDIATE_STATE, "State Board"),
                     )

BATCH_CHOICES = [(i,i) for i in range(2000,2020)]

PRIVATE = 0
PUBLIC = 1
AIDED = 2
INSTITUTION_TYPE = ((PRIVATE, "Private"),
                    (PUBLIC, "Public"),
                    (AIDED, "Aided"),
                    )

FATHER = 0
MOTHER = 1
ELDER_BROTHER = 2
YOUGER_BROTHER = 3
ELDER_SISTER = 4
YOUNGER_SISTER = 5
RELATION_CHOICES = ((FATHER, "Father"),
                    (MOTHER, "Mother"),
                    (ELDER_BROTHER, "Elder Brother"),
                    (YOUGER_BROTHER, "Younger Brother"),
                    (ELDER_SISTER, "Elder Sister"),
                    (YOUNGER_SISTER, "Younger Sister"))

OWN = 0
RENTED = 1
OWNERSHIP_CHOICES = ((OWN, "Own"),
                     (RENTED, "Rented"))

CONCRETE_ROOF = 0
THATCHED_HUT = 1
TILES = 2
HOUSE_TYPE_CHOICES = ((CONCRETE_ROOF, "Concrete roof"),
                      (THATCHED_HUT, "Thatched Hut"),
                      (TILES, "Tiles"),)

YES = 0
NO = 1
YES_NO_CHOICES = ((YES, "Yes"),
                  (NO, "No"))

YES = 0
NO = 1
NOT_SURE = 2
YES_NO__NOT_SURE_CHOICES = ((YES, "Yes"),
                            (NO, "No"),
                            (NOT_SURE, "Not sure"),)

NOT_YET_VERIFIED = 0
VERIFIED = 1
VERIFICATION_STATUS_CHOICES = ((NOT_YET_VERIFIED, "Not yet verified"),
                               (VERIFIED, "Verified"),)

LOAN = 0
GRANT = 1
SCHOLARSHIP_SCHEME_REPYAMENT_TYPE = ((LOAN, "Loan"), 
                                     (GRANT, "Grant"),)

YES = 0
NO = 1
PUBLISH_STATUS = ((YES, "Yes"), 
                             (NO, "No"),)


class ScholarshipApplication(models.Model):
    person = models.ForeignKey(Person)
    date_of_submission = models.DateTimeField(null=True, blank=True, auto_now=True)
    year_of_submission = models.IntegerField(null=True, blank=True, default=datetime.now().year)
    #personal details
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.IntegerField(choices=SEX_CHOICES, default = MALE, null=True, blank=True)
    roll_num = models.IntegerField(null=True, blank=True)
    #contact details in adittion to what stored in the Persons table
    hostel_address = models.TextField(null=True, blank=True)
    parent_contact = models.CharField(max_length=20, null=True, blank=True)
    #ssc details
    ssc_board = models.IntegerField(verbose_name="10th Board", choices=SSC_BOARD_CHOICES, default = SSC_CBSE, null=True, blank=True)
    ssc_batch = models.IntegerField(verbose_name="Year of passing", 
                                    choices=BATCH_CHOICES, default=2005, null=True, blank=True)
    ssc_percentage = models.DecimalField(verbose_name="Percentage(%)", null=True, blank=True, 
                                        max_digits=5, decimal_places=2)
    ssc_school_name = models.CharField(verbose_name="10th School Name", max_length=100, null=True, blank=True)
    ssc_school_address = models.TextField(verbose_name="10th School Address", null=True, blank=True)
    ssc_school_type = models.IntegerField(verbose_name="10th School Type", choices=INSTITUTION_TYPE, default=PRIVATE, null=True, blank=True)
    #intermediate_details
    intermediate_board = models.IntegerField(choices=INTERMEDIATE_BOARD_CHOICES,
                                             default = INTERMEDIATE_CBSE, null=True, blank=True)
    intermediate_batch = models.IntegerField(verbose_name="Year of passing", 
                                             choices=BATCH_CHOICES, default=2005, null=True, blank=True)
    intermediate_percentage = models.DecimalField(verbose_name="Percentage(%)", 
                                                  null=True, blank=True, max_digits=5, decimal_places=2)
    intermediate_college_name = models.CharField(max_length=100, null=True, blank=True)
    intermediate_college_address = models.TextField(null=True, blank=True)
    intermediate_college_type = models.IntegerField(choices=INSTITUTION_TYPE, 
                                                    default=PRIVATE, null=True, blank=True)
    #aieee
    aieee_air = models.IntegerField(null=True, blank=True)
    #vehicles
    has_two_wheeler = models.BooleanField(blank=True)
    has_four_wheeler = models.BooleanField(blank=True)
    #house_applicances
    has_tv = models.BooleanField(blank=True)
    has_fridge = models.BooleanField(blank=True)
    has_washing_machine = models.BooleanField(blank=True)
    house_ownership = models.IntegerField(choices=OWNERSHIP_CHOICES, null=True, blank=True)
    house_type = models.IntegerField(choices=HOUSE_TYPE_CHOICES, null=True, blank=True)
    agriculture_land = models.CharField(max_length=50, null=True, blank=True,
                                        help_text="Eg : We have 2.5 acres ")
    other_asset = models.TextField(null=True, blank=True, help_text="Eg : We have 8 cows and a tractor")
    question1 = models.TextField(null=True, blank=True, verbose_name = "How have you supported your education \
                                    till now and why are you applying for the \
                                    Lakshya scholarship?")
    question2 = models.TextField(null=True, blank=True, verbose_name = "How will you manage if \
                                you are not supported by Lakshya")
    #others
    
    status = models.IntegerField(choices=SCHOLARSHIP_APPLICATION_STATUS, 
                                 default=YET_TO_SHORTLIST, null=True, blank=True)

    def get_first_name(self):
        if self.person:
            return self.person.user.first_name
        else:
            return ""
    get_first_name.short_description = "First Name"
    
    def get_batch(self):
        if self.person:
            return self.person.year_of_passing
        else:
            return ""
    get_batch.short_description = "Batch"
    
    def get_branch(self):
        if self.person:
            return self.person.get_department_display()
        else:
            return ""
    get_branch.short_description = "Branch"
    
    def get_permanent_address(self):
        if self.person:
            return self.person.billing_address + "," + self.person.billing_landmark + "," + \
                    self.person.billing_city + "," + self.person.billing_state
        else:
            return ""
    get_permanent_address.short_description = "Permanent Address"
    
    def get_email_address(self):
        if self.person:
            return self.person.user.email
        else:
            return ""
    get_email_address.short_description = "Email Address"
    
    def get_contact_number(self):
        if self.person:
            return self.person.contact_number
        else:
            return ""
    get_contact_number.short_description = "Contact num"
    
    def __unicode__(self):
        return self.person.user.first_name

class Sgpa(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="sgpa")
    semester = models.IntegerField(choices=SEMESTER_CHOICES, null=True, blank=True)
    sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

class OtherExamPerformance(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="otherexams")
    exam_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(verbose_name="Year of exam", 
                               choices=BATCH_CHOICES, default=2005, null=True, blank=True)
    result = models.CharField(max_length=50, verbose_name="Rank/Percentage", null=True, blank=True)

class FamilyDetail(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="familydetails")
    name = models.CharField(max_length=100, null=True, blank=True)
    relation = models.IntegerField(choices=RELATION_CHOICES, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(verbose_name="Occupation", 
                                               max_length=200, help_text="", null=True, blank=True)
    annualincome = models.CharField(verbose_name="Annual Income", 
                                               max_length=200, help_text="", null=True, blank=True)
    

class OtherScholarship(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="otherscholarships")
    name = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True, 
                                help_text="Eg: I have applied for scholarship but \
                                 I am not sure if I will get it")


class ScholarshipVerification(models.Model):
    application = models.ForeignKey(ScholarshipApplication)
    verifier = models.ForeignKey(Person)
    date_of_verfication = models.DateField(null=True, blank=True)
    #whom all you have met
    met_applicant = models.BooleanField(blank=True)
    met_father = models.BooleanField(blank=True)
    met_mother = models.BooleanField(blank=True)
    met_siblings = models.BooleanField(blank=True)
    met_relatives = models.BooleanField(blank=True)
    met_neighbours = models.BooleanField(blank=True)
    house_ownership_type = models.IntegerField(verbose_name="Ownership of house where applicant is staying", 
                                               choices=OWNERSHIP_CHOICES, null=True, blank=True)
    house_type = models.IntegerField(verbose_name="Type of house where applicant is staying",
                                     choices=HOUSE_TYPE_CHOICES, null=True, blank=True)
    #all electronics the applicant has
    has_tv = models.BooleanField(blank=True)
    has_fridge = models.BooleanField(blank=True)
    has_washing_machine = models.BooleanField(blank=True)
    has_air_cooler = models.BooleanField(blank=True)
    has_air_conditioner = models.BooleanField(blank=True)
    vehicles_owned = models.CharField(max_length=200, null=True, blank=True, help_text="Eg:Bike, Cycle etc")
    #financial details
    father_details = models.TextField(verbose_name="About father's education, occupation and annual income", 
                                      null=True, blank=True)
    mother_details = models.TextField(verbose_name="About mother's education, occupation and annual income", 
                                      null=True, blank=True)
    sibling_details = models.TextField(verbose_name="About siblings of the applicant", 
                                      null=True, blank=True)    
    question1 = models.TextField(null=True, blank=True, verbose_name = "How has he supported his education till now",
                                 help_text="SSC, Intermidiate and Engineering till now")
    question2 = models.TextField(null=True, blank=True, verbose_name = "How does he plan to support \
                                             his education now if he doesn't get a Lakshya scholarship")
    aware_repayment_model = models.IntegerField(verbose_name="Is applicant and his family aware of the repayment model",
                                                choices=YES_NO_CHOICES, help_text="5 years time, no interest, no collateral",
                                                null=True, blank=True)
    aware_renewal_criteria = models.IntegerField(verbose_name="Is applicant and his family aware of the \
                                                scholarship renewal criteria", choices=YES_NO_CHOICES, help_text=" \
                                                If his performance is bad(fails in a subject or SGPA is less than 6) \
                                                for two consecutive semesters, then we will discontinue the scholarship",
                                                null=True, blank=True)
    final_recommendation = models.IntegerField(verbose_name="Recommendation",
                                               help_text = "Do you recommend this applicant for Lakshya scholarship?",
                                               choices=YES_NO__NOT_SURE_CHOICES,null=True, blank=True)
    additional_comment = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=VERIFICATION_STATUS_CHOICES, null=True, blank=True)
    
    def get_verifier_name(self):
        if self.verifier:
            return self.verifier.user.first_name
        else:
            return ""
    get_verifier_name.short_description = "First Name"
    
    def get_verifier_mobile_num(self):
        if self.verifier:
            return self.verifier.contact_number
        else:
            return ""
    get_verifier_mobile_num.short_description = "Mobile Number"    
    
    def get_verifier_email(self):
        if self.verifier:
            return self.verifier.user.email
        else:
            return ""
    get_verifier_email.short_description = "Email"   
    
    def get_applicant_name(self):
        if self.verifier:
            return self.application.person.user.first_name
        else:
            return ""
    get_applicant_name.short_description = "First name"     
    
    def __unicode__(self):
        return self.verifier.user.first_name + "-" + self.application.person.user.first_name 

class Scholar(models.Model):
    person = models.ForeignKey(Person)
    application = models.ForeignKey(ScholarshipApplication)
    donation_fund = models.ForeignKey(DonationFund, null=True, blank=True)
    
    def __unicode__(self):
        return self.person.user.first_name
    
    def name(self):
        return self.person.name()
    
    def batch(self):
        return str(self.person.year_of_passing - 4) + " - " + str(self.person.year_of_passing) + " batch" 
    
    def cgpa(self):
        if ScholarAcademicUpdate.objects.filter(scholar = self).order_by("-semester"):
            return str(ScholarAcademicUpdate.objects.filter(scholar = self).order_by("-semester")[0].cgpa)
        return "NA"
    
    def funding_amount(self):
        ret_val = ScholarshipPayment.objects.filter(scholar = self).aggregate(Sum('amount'))["amount__sum"]
        if ret_val :
            return str(ret_val)
        return "---" 
    
    def repaid_amount(self):
        ret_val = Repayment.objects.filter(scholar = self).aggregate(Sum('amount'))["amount__sum"]
        if ret_val :
            return str(ret_val)
        return "---" 
    
    def updates(self):
        ret_val = []
        for update in ScholarUpdate.objects.filter(scholar = self).order_by('-date_of_update'):
            ret_val.append(update.update)
        return ret_val
    
    def ssc_percentage(self):
        percentage = self.application.ssc_percentage
        if percentage:
            return str(percentage) + " %"
        
        return "NA"
    
    def inter_percentage(self):
        percentage = self.application.intermediate_percentage
        if percentage:
            return str(percentage) + " %"
        
        return "NA"
    
    def aieee_rank(self):
        aieee_rank = self.application.aieee_air
        
        if aieee_rank:
            return aieee_rank
        
        return "NA"
    
    def sgpa_list(self):
        ret_val = []
        for i in range(1,9):
            try:
                ret_val.append(ScholarAcademicUpdate.objects.get(scholar=self, semester=i).sgpa)
            except:
                ret_val.append("-")
        return ret_val
    
    def cgpa_list(self):
        ret_val = []
        for i in range(1,9):
            try:
                ret_val.append(ScholarAcademicUpdate.objects.get(scholar=self, semester=i).cgpa)
            except:
                ret_val.append("-")
        return ret_val
    
    def save(self, **kwargs):
        if not self.id:
            self.person = self.application.person
        super(Scholar, self).save(**kwargs)    


class ScholarshipPayment(models.Model):
    scholar = models.ForeignKey(Scholar)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default=THIRD_SEMESTER)
    payment_reason = models.IntegerField(choices=SCHOLARSHIP_PAYMENT_REASON, 
                                         default=TUTION_FEES)
    expense = models.ForeignKey(Expense)

    def __unicode__(self):
        return str(self.scholar) + " : Rs " + str(self.amount) +  " : " +str(self.expense.date_of_expense)

    def save(self, **kwargs):
        if not self.id:
            self.amount = self.expense.amount
        super(ScholarshipPayment, self).save(**kwargs)
        
class ScholarUpdate(models.Model):
    scholar = models.ForeignKey(Scholar)
    date_of_update = models.DateField(null=True, blank=True,)
    update = models.TextField()

    
class ScholarAcademicUpdate(models.Model):
    scholar = models.ForeignKey(Scholar)
    semester = models.IntegerField(choices=SEMESTER_CHOICES,)
    sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    comments = models.TextField(blank=True)
    
    def get_link(self):
        if self.id:
            return "<a href='/admin/scholarships/scholaracademicupdate/%d'>%d</a>" % (self.id, self.id)
        else:
            return ""
    get_link.allow_tags = True
    
    def __unicode__(self):
        return str(self.scholar.person.user.first_name) + " - " + str(self.get_semester_display())
    
class GradeUpdate(models.Model): 
    academic_update = models.ForeignKey(ScholarAcademicUpdate)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    comments = models.CharField(max_length=100, blank=True)
    
    
class Repayment(models.Model): 
    scholar = models.ForeignKey(Scholar)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_repayment = models.DateField()
    transacation_type = models.IntegerField(choices=TRANSACTION_CHOICES,)
    transaction_details = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return str(self.scholar) + " : Rs " + str(self.amount) +  " : " +str(self.date_of_repayment)
    
class ScholarshipScheme(models.Model):
    name = models.CharField("Scholarship Name", max_length = 150)
    funding_agency = models.CharField(max_length = 150)
    logo = models.FileField("Logo", upload_to="scholarships/schemes/logos", null=True, blank=True)
    repayment_type = models.IntegerField("Scholarship Type", choices = SCHOLARSHIP_SCHEME_REPYAMENT_TYPE)
    scholarship_amount = models.IntegerField(null=True, blank=True, help_text = "calculated annually")
    eligibility_criteria = models.URLField(null=True, blank=True)
    how_to_apply = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_mobile = models.CharField(max_length=30, null=True, blank=True)
    publish_status = models.IntegerField("Do you want to publish", choices=PUBLISH_STATUS, default=NO)
    curator = models.ForeignKey(User, null=True, blank=True, help_text = "Person entering the details")
    last_updated = models.DateField(auto_now=True)
    
    
    

    
    
    