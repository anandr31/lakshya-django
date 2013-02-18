from django.db import models
from people.models import Person

ENTERED = 0
APPROVED = 1
CLOSED = 2
REJECTED = 3
EXPENSE_STATUS_CHOICES = ((ENTERED, "Entered"),
                          (APPROVED, "Approved"),
                          (CLOSED, "Closed"),
                          (REJECTED, "Rejected"))

GENERAL = 0
SCHOLARSHIPS = 1
INNOVATION = 2
INTERNSHIPS = 3
ADMINISTRATION_EXPENSES = 4
EXPENSE_HEADER_FIRST_LEVEL_CHOICES = ((GENERAL, "General"),
                                (SCHOLARSHIPS, "Scholarships project"),
                                (INNOVATION, "Innovation project"),
                                (INTERNSHIPS, "Internships project"),
                                (ADMINISTRATION_EXPENSES, "Administrative Expenses"))


WEBSITE = 0
PUBLICITY = 1
SCHOLARSHIPS = 2
ACCOUNTING = 3
OTHERS = 4
SALARY = 5
EXPENSE_HEADER_SECOND_LEVEL_CHOICES = ((WEBSITE, "Website"),
                                       (PUBLICITY, "Publicity"),
                                       (SCHOLARSHIPS, "Scholarships"),
                                       (ACCOUNTING, "Accounting"),
                                       (SALARY, "Salary"),                                       
                                       (OTHERS, "Others"))


PAYMENT_GATEWAY = 1
CHEQUE = 2
DD = 3
CASH = 4
ONLINE_TRANSFER = 5
TRANSACTION_CHOICES = ((PAYMENT_GATEWAY, "Payment Gateway"),
                       (CHEQUE, "Cheque"),
                       (DD, "DD"),
                       (CASH, "Cash"),
                       (ONLINE_TRANSFER, "Online Transfer"))

DIRECT = 1
INDIRECT = 0
DONATION_TYPE = ((DIRECT, "Direct"),
                 (INDIRECT, "Indirect"),)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_expense = models.DateField()
    date_of_entry = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=EXPENSE_STATUS_CHOICES, default=ENTERED)
    expense_header_first_level = models.IntegerField(choices=EXPENSE_HEADER_FIRST_LEVEL_CHOICES, blank=True)
    expense_header_second_level = models.IntegerField(choices=EXPENSE_HEADER_SECOND_LEVEL_CHOICES, blank=True)
    scan_bill = models.FileField(upload_to="expenses", blank=True)
    details = models.TextField(blank=True)
    
    def header(self):
        return self.expense_header_first_level_display()
    
    def __unicode__(self):
        return str(self.date_of_expense) + " : Rs." + str(self.amount)


class DonationFund(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Donation Fund"
        verbose_name_plural = "Donation Fund"    

        
class Donation(models.Model):
    from scholarships.models import Scholar
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_donation = models.DateField()
    donor = models.ForeignKey(Person)
    donation_fund = models.ForeignKey(DonationFund, blank=True)
    transacation_type = models.IntegerField(choices=TRANSACTION_CHOICES,)
    transaction_details = models.CharField(max_length=200, blank=True) 
    donation_type = models.IntegerField(choices=DONATION_TYPE, default=DIRECT)
    pan_number = models.CharField(max_length=15, blank=True)
    is_repayment = models.BooleanField("Is this a repayment", default=False, help_text="Tick this only if its a repayment. Donar ~ Scholar for this donation")
    
    def get_donation_receipt(self):
        return "<a href='http://127.0.0.1:8000/accounts/donation-receipt'>Download</a>"
    get_donation_receipt.allow_tags = True 
    get_donation_receipt.short_description = "Donation Receipt"       
        
    def __unicode__(self):
        return str(self.date_of_donation) + " : Rs." + str(self.amount) + self.donor.user.first_name        
    
class PaymentTemp(models.Model):
    email_address = models.EmailField('Email Address')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    email_receipt = models.BooleanField("Email me the Donation Receipt", default=True)
    
class Pledge(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    batch = models.IntegerField("Year of Graduation", choices = [(x,x) for x in reversed(range(1964, 2013))])
    rs_or_dollar = models.IntegerField(choices = [(10000, "Rs 10,000"), (500, "$ 500"),])
    month_of_donation = models.CharField(choices=[("feb", "February, 2013"), ("mar", "March, 2013"), ("apr", "April, 2013"),], max_length="4")
    donation = models.ForeignKey(Donation, blank=True, null=True)
        
    