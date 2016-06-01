
from datetime import date, datetime

from django.db import models
from django.db.models.aggregates import Max
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

from people.models import Person
from lakshya.constants import CURRENCIES, C_INR
from lakshya.util import format_and_split_name, get_random_number, get_currency_iso_code


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
HACKATHON = 5
INNOVATION_GARAGE = 6
EXPENSE_HEADER_FIRST_LEVEL_CHOICES = ((GENERAL, "General"),
                                (SCHOLARSHIPS, "Scholarships"),
                                (INNOVATION, "Innovation Project"),
                                (INTERNSHIPS, "Internships"),
                                (ADMINISTRATION_EXPENSES, "Administrative Expenses"),
                                (HACKATHON, "Hackathon"),
                                (INNOVATION_GARAGE, "Innovation Garage"))


WEBSITE = 0
PUBLICITY = 1
SCHOLARSHIPS = 2
ACCOUNTING = 3
OTHERS = 4
SALARY = 5
TRAVEL = 6
EQUIPMENT = 7
CONSUMABLES = 8
EXPENSE_HEADER_SECOND_LEVEL_CHOICES = ((WEBSITE, "Website"),
                                       (PUBLICITY, "Publicity"),
                                       (SCHOLARSHIPS, "Scholarships"),
                                       (ACCOUNTING, "Accounting"),
                                       (SALARY, "Salary"),                                       
                                       (TRAVEL, "Travel"),
                                       (EQUIPMENT, "Equipment"),
                                       (CONSUMABLES, "Consumables"),
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
                                           help_text="'Cheque number xxx' or 'DD number xxx' or 'CCAvenue \
                                           Transaction ID number xxx'")
    donation_type = models.IntegerField(choices=DONATION_TYPE, default=DIRECT)
    is_repayment = models.BooleanField("Is this a repayment", default=False, help_text="Tick this only if its a repayment. Donor ~ Scholar for this donation")
    receipt_number = models.IntegerField(blank=True, null=True)

    def get_transaction_details(self):
        if self.bank_details:
            retval = "[%s]" % (self.bank_details,)
            if self.transaction_details:
                retval = "[%s, %s]" % (self.bank_details, self.transaction_details)
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
	    if self.date_of_donation.month in [1,2,3]:
		financial_year_1 = self.date_of_donation.year-1
		financial_year_2 = self.date_of_donation.year
	    else:
		financial_year_1 = self.date_of_donation.year
		financial_year_2 = self.date_of_donation.year+1
  	    date_1=date(financial_year_1, 4, 1)
	    date_2=date(financial_year_2, 3, 31)
            self.receipt_number = (Donation.objects.filter(date_of_donation__gte = date_1, date_of_donation__lte = date_2).aggregate(Max('receipt_number'))["receipt_number__max"] or 0) + 1
            super(Donation, self).save(**kwargs)
            return
        super(Donation, self).save(**kwargs)
    
class PaymentTemp(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    email_address = models.EmailField('Email')
    email_receipt = models.BooleanField("I want to save tax on this donation", default=False, help_text="What is 80G exemption?<br/>50% of donated amount is deductible from<br/>donor's taxable income.")
    pan_card = models.CharField("PAN", max_length=10, null=True, blank=True, help_text="Required for donation receipt")
    referrer_url = models.CharField("Referrer Field", max_length=100, null=True, blank=True)
    flex_field = models.CharField("Flexible Field", default="Donation to Lakshya", max_length=100, null=True, blank=True)
    pledge_id = models.IntegerField(blank=True, null=True, help_text='Only used for crowdfunding pledge fulfilment transactions')

    
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
        
class BankAccount(models.Model):
    bank = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_type = models.CharField(choices=[("savings", "Savings Account"), ("fd", "Fixed Deposit/Term Deposit"), ("fcra", "FCRA"),], max_length="10")
    contact_person = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=50)
    contact_phone = models.CharField(max_length=10)
   
    def __unicode__(self):
        return str(self.bank) + " " + str(self.account_type)

class BankBalance(models.Model):
    account = models.ForeignKey(BankAccount)
    date = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
class Milestone(models.Model):
  title = models.CharField(max_length=100)
  target_amount = models.DecimalField(max_digits=10, decimal_places=0)
  start_date = models.DateField()
  end_date = models.DateField()
  committed_amount = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, default=0)
  # raised_amount = models.ForeignKey(Donation, null=True, blank=True)

  def get_raised_amount(self):
    "Returns total amount raised"
    amount = Donation.objects.filter(donation_fund__name=self.title).aggregate(Sum("amount"))["amount__sum"]
    return (amount if amount else 0)
  
  raised_amount = property(get_raised_amount)

  def get_raised_percent(self):
    "Returns amount raised as a percent of target amount"
    if not self.raised_amount:
      return 0
    ratio = self.raised_amount / self.target_amount
    return float(ratio * 100)
  
  raised_precent = property(get_raised_percent)


# New structure for CCAvenue FCRA PG. Taking help from kalyan@almabase.com

class PGTransactionManager(models.Manager):
    def create_transaction(self, amount, currency, productinfo='', user=None, mode='', content_object=None):
        txnid = str(get_random_number(10))
        name = user.get_full_name() if user else ''
        email = user.email if user else ''
        txn = self.model.objects.create(creator=user, txnid=txnid, amount=amount, productinfo=productinfo,
                                                      mode=mode, name=name, email=email, phone='',
                                                      currency=currency, content_object=content_object)
        return txn


class PGTransaction(models.Model):
    """A payment gateway transaction."""
    #Transaction statuses
    TS_UNPROCESSED, TS_SUCCESS, TS_FAILED, TS_PENDING, TS_ERROR = 1, 2, 3, 4, 5
    TXN_STATUSES = ((TS_UNPROCESSED, "Unprocessed"), (TS_SUCCESS, "Success"),
                    (TS_FAILED, "Failed"), (TS_PENDING, "Pending"), (TS_ERROR, "Error"))

    creator = models.ForeignKey(User, null=True, blank=True)
    txnid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.SmallIntegerField(choices=CURRENCIES, default=C_INR)
    productinfo = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    request_hash = models.CharField(max_length=255, blank=True)
    mode = models.CharField(max_length=255, blank=True)
    #Response from PG
    pg_txnid = models.CharField(max_length=255, blank=True)
    status = models.SmallIntegerField(choices=TXN_STATUSES, default=TS_UNPROCESSED, null=True)
    error = models.CharField(max_length=255, blank=True)
    response_hash = models.CharField(max_length=255, blank=True)
    response_data = models.TextField(max_length=5000, blank=True)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(auto_now_add=True)

    objects = PGTransactionManager()

    class Meta:
        verbose_name = 'Payment Gateway Transaction'
        verbose_name_plural = 'Payment Gateway Transactions'

    def __unicode__(self):
        return self.txnid

    def get_first_name(self):
        return format_and_split_name(self.name)[0]

    def get_last_name(self):
        return format_and_split_name(self.name)[1]

    def has_user_details(self):
        #Name, email, mobile are mandatory fields. Return true if the transaction has all these details
        return self.name and self.email and self.phone

    def get_parent(self):
        return self.content_type
    parent = property(get_parent)

    def is_successful(self):
        return self.status == self.TS_SUCCESS


class FCRADonation(models.Model):
    donor = models.ForeignKey(Person, related_name='fcra_donations')
    transactions = generic.GenericRelation(PGTransaction)
    amount = models.IntegerField()
    currency = models.SmallIntegerField(choices=CURRENCIES, default=C_INR)
    donation_fund = models.ForeignKey(DonationFund, blank=True)
    transacation_type = models.IntegerField(choices=TRANSACTION_CHOICES,)
    donation_type = models.IntegerField(choices=DONATION_TYPE, default=DIRECT)
    bank_details = models.CharField(max_length=200, null=True, blank=True,
                                           help_text="Enter Bank and Branch Details. Mandatory \
                                           if Cheque or DD id choosen")
    is_repayment = models.BooleanField("Is this a repayment", default=False,
                        help_text="Tick this only if its a repayment. Donor ~ Scholar for this donation")
    receipt_number = models.IntegerField(blank=True, null=True)
    email_receipt = models.BooleanField(default=False)
    pan_card = models.CharField("PAN Card", max_length=10, null=True, blank=True)
    time = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'FCRA Donation'
        verbose_name_plural = 'FCRA Donations'

    def __unicode__(self):
        return ' for '.join(filter(None, [self.donor.user.get_full_name(),
                                          self.donation_fund.name if self.donation_fund else '']))

    def get_succesful_transactions(self):
        return self.transactions.filter(status=PGTransaction.TS_SUCCESS)

    def get_latest_succesful_transaction(self):
        return self.transactions.filter(status=PGTransaction.TS_SUCCESS).order_by('created').first()

    def get_currency_code(self):
        return get_currency_iso_code(self.currency)
    get_currency_code.short_description = 'Currency'

    def on_payment_response(self, txn):
        if txn.status == PGTransaction.TS_SUCCESS:
            self.completed = True
            self.save()

    def populate_context(self, context):
        context['title'] = 'Thank you for your donation'

    def get_payment_data(self):
        """Return a dict with necessary info to be shown for payment history"""
        return {'amount': self.amount, 'currency': self.currency, 'type': 'donation', 'time': self.time,
                'text': 'Donated to <a class="subtle" href="/fundraising/' + self.project.slug + '">' + \
                self.project.name + '</a>'}

    def save(self, **kwargs):
        if not self.receipt_number:
            if self.time.month in [1, 2, 3]:
                financial_year_1 = self.time.year - 1
                financial_year_2 = self.time.year
            else:
                financial_year_1 = self.time.year
                financial_year_2 = self.time.year + 1
            date_1 = date(financial_year_1, 4, 1)
            date_2 = date(financial_year_2, 3, 31)
            self.receipt_number = (FCRADonation.objects.filter(time__gte=date_1,
                                    time__lte=date_2).aggregate(Max('receipt_number'))["receipt_number__max"] or 0) + 1

        super(FCRADonation, self).save(**kwargs)
