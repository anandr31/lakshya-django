from django.db.models import Count
from django.contrib import admin
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from utils.models import LakshyaUpdate
from utils.models import LakshyaTestimonial
from innovationgarage.models import Event
from hackathon.models import *
from crowdfunding.models import *
from django.db.models import Sum
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect
from accounts.models import Expense, Donation, DonationFund, BankAccount, BankBalance, Milestone, PAYMENT_GATEWAY, \
    DIRECT
from people.models import Person
from collections import Counter

MIDDLE_EAST_COUNTRIES = ['Bahrain', 'Cyprus', 'Egypt', 'Iran', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia', 'Syria', 'Turkey', 'UAE', 'Yemen']
UNITED_STATES = ['USA', 'US', 'United States', 'United States of America']

def get_home_page(request):
    update_list = LakshyaUpdate.objects.filter(sorting__in = [1,2,3]).order_by('sorting')  
    total_donation_amount = Donation.objects.all().aggregate(Sum("amount"))["amount__sum"]
    testimonial_list=LakshyaTestimonial.objects.order_by('?')[:3]
    return render_to_response("index.html", 
                              RequestContext(request, {'update_list':update_list, 'total_donation_amount':total_donation_amount, 'testimonial_list':testimonial_list}))# Create your views here.


def server_error(request):
    response = render(request, "500.html")
    response.status_code = 500
    return response


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            donations = Donation.objects.all()
            expenses = Expense.objects.all()

            donor_details_list = [] #list of tuples - name, batch, branch, amount, last Donated on
            top_donor_details_list = [] #list of top donors
            freq_donor_details_list = [] #list of most frequent donors
            for temp_dict in Donation.objects.values('donor').annotate(total=Sum('amount')):
                donor_id = temp_dict["donor"]
                total = temp_dict["total"]
                donor = Person.objects.get(id=donor_id)
                count = Donation.objects.filter(donor=donor).count() ## top frequent donors
                last_donated_on = Donation.objects.filter(donor=donor).order_by("-date_of_donation")[0].date_of_donation
                donor_details = (donor.name, donor.year_of_passing, donor.get_department_display, total, last_donated_on)
                freq_donor_details = (donor.name, count, total)
                top_donor_details = (donor.name, total)
                donor_details_list.append(donor_details)
                if not donor_id in [26, 27]: # Excluding Anonymous and Bank Interest from these lists
                    top_donor_details_list.append(top_donor_details) ##
                    freq_donor_details_list.append(freq_donor_details) ##
            total_donation_amount = Donation.objects.all().aggregate(Sum("amount"))["amount__sum"]
            donor_distinct_set = set()
            for donation in Donation.objects.all():
                donor_distinct_set.add(donation.donor.id)
            total_donors = len(donor_distinct_set)

            avg_donation_amount = total_donation_amount / total_donors

            top_donor_details_list = sorted(top_donor_details_list, key=lambda donors: donors[1], reverse=True) ##
            del top_donor_details_list[4:] ##

            freq_donor_details_list = sorted(freq_donor_details_list, key=lambda donors: donors[1], reverse=True) ##
            # del freq_donor_details_list[4:] ##

            # Calculate annual and monthly donations...starts here
            monthly_donations = []
            annual_donations = []
            monthly_expenses = []
            annual_expenses = []            
            years = [2008,2009,2010,2011,2012,2013,2014,2015,2016]
            for year in years:
                # Donations
                object_by_year = Donation.objects.filter(date_of_donation__year=year)
                donation_list_by_year = object_by_year.aggregate(total=Sum('amount'))
                donations = (year, donation_list_by_year["total"])
                annual_donations.append(donations)
                donation_list_by_month = object_by_year.extra({'month' : "MONTH(date_of_donation)"}).values('month').annotate(total=Sum('amount')).order_by('month')
                for temp_dict in donation_list_by_month:
                    month = temp_dict["month"]
                    total = temp_dict["total"]
                    donations = (month, total)
                    monthly_donations.append(donations)                
                # Expenses
                object_by_year = Expense.objects.filter(date_of_expense__year=year)
                expenses_list_by_year = object_by_year.aggregate(total=Sum('amount'))
                expenses = (year, expenses_list_by_year["total"])
                annual_expenses.append(expenses)
                expenses_list_by_month = object_by_year.extra({'month' : "MONTH(date_of_expense)"}).values('month').annotate(total=Sum('amount')).order_by('month')
                for temp_dict in expenses_list_by_month:
                    month = temp_dict["month"]
                    total = temp_dict["total"]
                    expenses = (month, total)
                    monthly_expenses.append(expenses)                
            # ...ends here

            # Calculate donations by Geography... starts here
            india_donation = Donation.objects.filter(donor__billing_country='India').aggregate(total=Sum('amount'))['total']
            usa_donation = Donation.objects.filter(donor__billing_country__in = UNITED_STATES).aggregate(total=Sum('amount'))['total']
            me_donation = Donation.objects.filter(donor__billing_country__in = MIDDLE_EAST_COUNTRIES).aggregate(total=Sum('amount'))['total']
            total_donations = Donation.objects.all().aggregate(total = Sum('amount'))['total']
            donation_by_geo_list = (('India', india_donation, 100*india_donation/total_donations), 
                            ('USA', usa_donation, 100*usa_donation/total_donations), ('ME', me_donation, 100*me_donation/total_donations))
            # ... ends here

            # Calculate number of unique donors by geo.. starts here
            donor_distinct_set_india = set()
            for donation in Donation.objects.filter(donor__billing_country='India'):
                donor_distinct_set_india.add(donation.donor.id)
            india_donors = len(donor_distinct_set_india)
            
            donor_distinct_set_usa = set()
            for donation in Donation.objects.filter(donor__billing_country__in = UNITED_STATES):
                donor_distinct_set_usa.add(donation.donor.id)
            usa_donors = len(donor_distinct_set_usa)

            donor_distinct_set_me = set() # ME = Middle East
            for donation in Donation.objects.filter(donor__billing_country__in = MIDDLE_EAST_COUNTRIES):
                donor_distinct_set_me.add(donation.donor.id)
            me_donors = len(donor_distinct_set_me)    

            donors_by_geo_list = (('India', india_donors, 100*india_donors/total_donors), 
                                  ('USA', usa_donors, 100*usa_donors/total_donors), 
                                  ('ME', me_donors, 100*me_donors/total_donors))
            # ... ends here

            # Measuring Event stats... starts here
            monthly_participation = []
            events = Event.objects.all()
            total_participation = events.aggregate(Sum('participation'))["participation__sum"]
            total_events_count = len(events)
            monthly_participation_list = events.extra({'month' : "MONTH(date)"}).values('month').annotate(total=Sum('participation')).order_by('month')
            for temp_dict in monthly_participation_list:
                month = temp_dict["month"]
                count = temp_dict["total"]
                participation = (month, count)
                monthly_participation.append(participation)
            # ends here

            # Sort donors by frequency of donation... starts here
            freq_details_list = Counter(elem[1] for elem in freq_donor_details_list)
            donated_once = sum(v for k, v in freq_details_list.iteritems() if k == 1)
            donated_twice = sum(v for k, v in freq_details_list.iteritems() if k == 2)
            donated_more_than_twice = sum(v for k, v in freq_details_list.iteritems() if k > 2)
            
            freq_of_donation_stats = (('Once',donated_once, 100*donated_once/total_donors), 
                                      ('Twice',donated_twice, 100*donated_twice/total_donors), 
                                      ('More than twice',donated_more_than_twice, 100*donated_more_than_twice/total_donors))
            # ...ends here

            # Show bank balance details... starts here
            bank_balance_list = []
            for account in BankAccount.objects.all():
                balance_amount = BankBalance.objects.filter(account=account).reverse()[0].balance
                date = BankBalance.objects.filter(account=account).reverse()[0].date
                temp_list = (account.bank, account.get_account_type_display, date, balance_amount)
                bank_balance_list.append(temp_list)
            # ...ends here

            # Track milestones... starts here
            milestones = Milestone.objects.all()
            # ...ends here


            context = {"donor_details_list" : donor_details_list,
                        "total_donation_amount" : total_donation_amount,
                        "total_donors" : total_donors,
                        "avg_donation_amount" : avg_donation_amount,
                        "top_donor_details_list" : top_donor_details_list,
                        "freq_donor_details_list" : freq_donor_details_list,
                        "monthly_donations": monthly_donations,
                        "annual_donations": annual_donations,
                        "monthly_expenses": monthly_expenses,
                        "annual_expenses": annual_expenses,
                        "donations": donations,
                        "expenses": expenses,
                        "events": events,
                        "total_participation": total_participation,
                        "total_events_count": total_events_count,
                        "monthly_participation": monthly_participation,
                        "donors_by_geo_list": donors_by_geo_list,
                        "donation_by_geo_list": donation_by_geo_list,
                        "freq_of_donation_stats": freq_of_donation_stats,
                        "bank_balance_list": bank_balance_list,
                        "milestones": milestones
                        }

            return context
        else:
            raise Http404

class HomeView(TemplateView):
    template_name = 'lakshya/home.html'

    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next', '')
        if next_url and next_url.startswith('/'):
            return HttpResponseRedirect(next_url)
        return super(HomeView, self).get(request, *args, **kwargs)
