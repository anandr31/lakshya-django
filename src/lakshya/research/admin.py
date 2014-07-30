'''
Created on 14-Jul-2013

@author: srihari
'''
from django.contrib import admin
from models import ConferenceApplication, InternshipApplication
from research.models import Panelist, ConferenceApplicationFeedback

class PanelistAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "active",)
    list_filter = ("branch", "active",)

class ConferenceApplicationAdmin(admin.ModelAdmin):
    fieldsets = [("Basic Details", {"fields" : [('date_of_submission', 'status',),]}),
                 ("Conference Details", {"fields" : ['conference_name', 'conference_dates', 'expected_expenditure',
                                                     'conference_city', 'conference_country',]}),
                 ("Application Details", {"fields" : ['paper_title', 'sop', 'acceptance_email']}),
                 ("Applicant Details", {"fields" : ['get_applicant_detail', 'applicant',]}),
                 ("Review Details", {"fields" : ['review',]}),]
    raw_id_fields = ('applicant',)
    list_display = ('paper_title', 'year_of_submission', 'status',)
    list_filter = ('year_of_submission', 'status', 'conference_name', 'conference_country')
    readonly_fields = ("get_applicant_detail", "date_of_submission", )
    
class InternshipApplicationAdmin(admin.ModelAdmin):
    fieldsets = [("Basic Details", {"fields" : [('date_of_submission', 'status',),]}),
                 ("Internship Details", {"fields" : ['internship_place', 'internship_division', 'supervisor_name', 'expected_expenditure',
                                                     'internship_dates', 'internship_city', 'internship_country',]}),
                 ("Applicant Details", {"fields" : ['get_applicant_detail', 'applicant',]}),
                 ("Review Details", {"fields" : ['review',]}),]
    raw_id_fields = ('applicant',)
    list_display = ('internship_place', 'year_of_submission', 'status',)
    list_filter = ('year_of_submission', 'status', 'internship_place', 'internship_country')
    readonly_fields = ("get_applicant_detail", "date_of_submission", )
    
class ConferenceApplicationFeedbackAdmin(admin.ModelAdmin):
    list_display = ("application", "panelist", "recommended_extent_of_funding",)
    list_filter = ("recommended_extent_of_funding",)
    
admin.site.register(InternshipApplication, InternshipApplicationAdmin)
admin.site.register(ConferenceApplication, ConferenceApplicationAdmin)
admin.site.register(Panelist, PanelistAdmin)
admin.site.register(ConferenceApplicationFeedback, ConferenceApplicationFeedbackAdmin)


