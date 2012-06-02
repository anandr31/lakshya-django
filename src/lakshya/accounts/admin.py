from accounts.models import Expense, DonationFund, Donation
from django.contrib import admin

class ExpenseOptions(admin.ModelAdmin):
    list_display = ('amount', 'date_of_expense', 'expense_header_first_level', "expense_header_second_level", "status",)
    list_filter = ('expense_header_first_level', 'expense_header_second_level', "status", )
    date_hierarchy = 'date_of_expense'

class DonationFundOptions(admin.ModelAdmin):
    list_display = ('name', 'description', )
    
class DonationOptions(admin.ModelAdmin):
    list_display = ('amount', 'date_of_donation', 'donor', )
    list_filter = ('transacation_type', )
    search_fields = ('donor__user__first_name', )
    raw_id_fields = ('donor', 'donation_fund',)
    
    
admin.site.register(Expense, ExpenseOptions)
admin.site.register(DonationFund, DonationFundOptions)
admin.site.register(Donation, DonationOptions)