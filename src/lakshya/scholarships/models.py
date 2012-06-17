from django.db import models
from people.models import Person
from datetime import datetime
from accounts.models import DonationFund, Expense, TRANSACTION_CHOICES

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

class ScholarshipApplication(models.Model):
    person = models.ForeignKey(Person)
    date_of_submission = models.DateTimeField()
    year_of_submission = models.IntegerField()
    #personal details
    date_of_birth = models.DateField(blank=True)
    sex = models.IntegerField(choices=SEX_CHOICES, default = MALE)
    roll_num = models.IntegerField(blank=True)
    #contact details in adittion to what stored in the Persons table
    hostel_address = models.TextField(blank=True)
    parent_contact = models.CharField(max_length=20)
    #ssc details
    ssc_board = models.IntegerField(choices=SSC_BOARD_CHOICES, default = SSC_CBSE)
    ssc_batch = models.IntegerField(verbose_name="Year of passing", 
                                    choices=BATCH_CHOICES, default=2005)
    ssc_percentage = models.DecimalField(verbose_name="Percentage(%)", blank=True,
                                        max_digits=5, decimal_places=2)
    ssc_school_name = models.CharField(max_length=100, blank=True)
    ssc_school_address = models.TextField(blank=True)
    ssc_school_type = models.IntegerField(choices=INSTITUTION_TYPE, default=PRIVATE)
    #intermediate_details
    intermediate_board = models.IntegerField(choices=INTERMEDIATE_BOARD_CHOICES,
                                             default = INTERMEDIATE_CBSE)
    intermediate_batch = models.IntegerField(verbose_name="Year of passing", 
                                             choices=BATCH_CHOICES, default=2005)
    intermediate_percentage = models.DecimalField(verbose_name="Percentage(%)", 
                                                  blank=True, max_digits=5, decimal_places=2)
    intermediate_college_name = models.CharField(max_length=100, blank=True)
    intermediate_college_address = models.TextField(blank=True)
    intermediate_college_type = models.IntegerField(choices=INSTITUTION_TYPE, 
                                                    default=PRIVATE)
    #aieee
    aieee_air = models.IntegerField(blank=True)
    #vehicles
    has_two_wheeler = models.BooleanField(blank=True)
    has_four_wheeler = models.BooleanField(blank=True)
    #house_applicances
    has_tv = models.BooleanField(blank=True)
    has_fridge = models.BooleanField(blank=True)
    has_washing_machine = models.BooleanField(blank=True)
    house_ownership = models.IntegerField(choices=OWNERSHIP_CHOICES, blank=True)
    house_type = models.IntegerField(choices=HOUSE_TYPE_CHOICES, blank=True)
    agriculture_land = models.CharField(max_length=50, blank=True,
                                        help_text="Eg : We have 2.5 acres ")
    other_asset = models.TextField(blank=True, help_text="Eg : We have 8 cows and a tractor")
    question1 = models.TextField(blank=True, verbose_name = "How have you supported your education \
                                    till now and why are you applying for the \
                                    Lakshya scholarship?")
    question2 = models.TextField(blank=True, verbose_name = "How will you manage if \
                                you are not supported by Lakshya")
    #others
    
    status = models.IntegerField(choices=SCHOLARSHIP_APPLICATION_STATUS, 
                                 default=YET_TO_SHORTLIST)

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
            return self.person.department
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

class Sgpa(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="sgpa")
    semester = models.IntegerField(choices=SEMESTER_CHOICES, blank=True)
    sgpa = models.DecimalField(max_digits=4, decimal_places=2)

class OtherExamPerformance(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="otherexams")
    exam_name = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(verbose_name="Year of exam", 
                               choices=BATCH_CHOICES, default=2005)
    result = models.CharField(max_length=50, verbose_name="Rank/Percentage", blank=True)

class FamilyDetail(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="familydetails")
    name = models.CharField(max_length=100, blank=True)
    relation = models.IntegerField(choices=RELATION_CHOICES, blank=True)
    education = models.CharField(max_length=100, blank=True)
    occupation_annualincome = models.CharField(verbose_name="Occupation & Annual Income", 
                                               max_length=200, help_text="", blank=True)
    

class OtherScholarship(models.Model):
    application = models.ForeignKey(ScholarshipApplication, related_name="otherscholarships")
    name = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.CharField(max_length=200, blank=True, 
                                help_text="Eg: I have applied for scholarship but \
                                 I am not sure if I will get it")


class ScholarshipVerification(models.Model):
    application = models.ForeignKey(ScholarshipApplication)
    verifier = models.ForeignKey(Person)
    date_of_verfication = models.TimeField(blank=True)
    #whom all you have met
    met_applicant = models.BooleanField(blank=True)
    met_father = models.BooleanField(blank=True)
    met_mother = models.BooleanField(blank=True)
    met_siblings = models.BooleanField(blank=True)
    met_relatives = models.BooleanField(blank=True)
    met_neighbours = models.BooleanField(blank=True)
    house_ownership_type = models.IntegerField(verbose_name="Ownership of house where applicant is staying", 
                                               choices=OWNERSHIP_CHOICES, blank=True)
    house_type = models.IntegerField(verbose_name="Type of house where applicant is staying",
                                     choices=HOUSE_TYPE_CHOICES, blank=True)
    #all electronics the applicant has
    has_tv = models.BooleanField(blank=True)
    has_fridge = models.BooleanField(blank=True)
    has_washing_machine = models.BooleanField(blank=True)
    has_air_cooler = models.BooleanField(blank=True)
    has_air_conditioner = models.BooleanField(blank=True)
    vehicles_owned = models.CharField(max_length=200, blank=True, help_text="Eg:Bike, Cycle etc")
    #financial details
    father_details = models.TextField(verbose_name="About father's education, occupation and annual income", 
                                      blank=True)
    mother_details = models.TextField(verbose_name="About mother's education, occupation and annual income", 
                                      blank=True)
    sibling_details = models.TextField(verbose_name="About siblings of the applicant", 
                                      blank=True)    
    question1 = models.TextField(blank=True, verbose_name = "How has he supported his education till now",
                                 help_text="SSC, Intermidiate and Engineering till now")
    question2 = models.TextField(blank=True, verbose_name = "How does he plan to support \
                                             his education now if he doesn't get a Lakshya scholarship")
    aware_repayment_model = models.IntegerField(verbose_name="Is applicant and his family aware of the repayment model",
                                                choices=YES_NO_CHOICES, help_text="5 years time, no interest, no collateral")
    aware_renewal_criteria = models.IntegerField(verbose_name="Is applicant and his family aware of the \
                                                scholarship renewal criteria", choices=YES_NO_CHOICES, help_text=" \
                                                If his performance is bad(fails in a subject or SGPA is less than 6) \
                                                for two consecutive semesters, then we will discontinue the scholarship")
    final_recommendation = models.IntegerField(verbose_name="Do you recommend this applicant for Lakshya scholarship?",
                                               choices=YES_NO__NOT_SURE_CHOICES,)
    additional_comment = models.TextField(blank=True)
    

class Scholar(models.Model):
    scholar = models.ForeignKey(Person)
    application = models.ForeignKey(ScholarshipApplication)
    donation_fund = models.ForeignKey(DonationFund)


class ScholarshipPayment(models.Model):
    scholar = models.ForeignKey(Scholar)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default=THIRD_SEMESTER)
    payment_reason = models.IntegerField(choices=SCHOLARSHIP_PAYMENT_REASON, 
                                         default=TUTION_FEES)
    expense = models.ForeignKey(Expense)


class ScholarUpdate(models.Model):
    scholar = models.ForeignKey(Scholar)
    date_of_update = models.DateField(null=True, blank=True, auto_now_add=True)
    update = models.TextField()

    
class ScholarAcademicUpdate(models.Model):
    scholar = models.ForeignKey(Scholar)
    sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    comments = models.TextField(blank=True)

    
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