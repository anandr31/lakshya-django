from django.db import models
from people.models import Person
from django.db.models.aggregates import Max


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

EXPENSE_PAYMENT_TYPE = ((DIRECT, "Direct"),
                 (INDIRECT, "Indirect"),)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_expense = models.DateField()
    date_of_entry = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=EXPENSE_STATUS_CHOICES, default=ENTERED)
    expense_header_first_level = models.IntegerField(choices=EXPENSE_HEADER_FIRST_LEVEL_CHOICES, blank=True)
    expense_header_second_level = models.IntegerField(choices=EXPENSE_HEADER_SECOND_LEVEL_CHOICES, blank=True)
    scan_bill = models.FileField(upload_to="expenses", blank=True)
    details = models.TextField(blank=True, null=True)
    payment_type = models.IntegerField(choices=EXPENSE_PAYMENT_TYPE, default=DIRECT)
    transaction_number = models.CharField(max_length=100, null=True, blank=True, help_text="Check/DD No")
    
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
    bank_details = models.CharField(max_length=200, null=True, blank=True,
                                           help_text="Enter Bank and Branch Details. Mandatory \
                                           if Cheque or DD id choosen")
    transaction_details = models.CharField(max_length=200, null=True, blank=True,
                                           help_text="'Cheque number xxx' or 'DD number xxx' or the CCAvenue \
                                           Transaction ID")
    donation_type = models.IntegerField(choices=DONATION_TYPE, default=DIRECT)
    is_repayment = models.BooleanField("Is this a repayment", default=False, help_text="Tick this only if its a repayment. Donor ~ Scholar for this donation")
    receipt_number = models.IntegerField(blank=True, null=True)

    def get_transaction_details(self):
        if self.bank_details:
            retval = "[%s" % (self.bank_details,)
            if self.transaction_details:
                retval += ", %s" % (self.transaction_details) % "]"
            return retval
        else:
            return ""

    def get_donation_receipt(self):
        
        return "<a href='http://127.0.0.1:8000/accounts/donation-receipt'>Mail Receipt</a>"
    get_donation_receipt.allow_tags = True 
    get_donation_receipt.short_description = "Donation Receipt"       
        
    def __unicode__(self):
        return str(self.date_of_donation) + " : Rs." + str(self.amount) + self.donor.user.first_name        
    
    def save(self, **kwargs):
        if not self.pk:
            #We need to create the invoice number when its getting created
            self.receipt_number = (Donation.objects.filter(date_of_donation__year = self.date_of_donation.year).aggregate(Max('receipt_number'))["receipt_number__max"] or 0) + 1
            super(Donation, self).save(**kwargs)
            return
        super(Donation, self).save(**kwargs)
    
class PaymentTemp(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    email_address = models.EmailField('Email')
    email_receipt = models.BooleanField("I want to save tax on this donation", default=False, help_text="What is 80G exemption?<br/>50% of donated amount is deductible from<br/>donor's taxable income.")
    pan_card = models.CharField("PAN", max_length=10, null=True, blank=True, help_text="Required for donation receipt")

    
class Pledge(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    batch = models.IntegerField("Year of Graduation", choices = [(x,x) for x in reversed(range(1964, 2013))])
    rs_or_dollar = models.IntegerField(choices = [(10000, "Rs 10,000"), (500, "$ 500"),], blank=True)
    month_of_donation = models.CharField(choices=[("may", "May, 2013"), ("jun", "June, 2013"), ("jul", "July, 2013"),
                                                  ("aug", "Aug, 2013"), ("sep", "Sept, 2013"), ("oct", "Oct, 2013"),], max_length="4")
    has_donated = models.BooleanField(default=False,)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    donation = models.ForeignKey(Donation, blank=True, null=True)
        
    
