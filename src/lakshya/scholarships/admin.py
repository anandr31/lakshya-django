from django.contrib import admin
from scholarships.models import ScholarshipApplication, ScholarshipVerification,\
    Scholar, ScholarshipPayment, Repayment, Sgpa, OtherExamPerformance,\
    FamilyDetail, OtherScholarship, ScholarUpdate, ScholarAcademicUpdate,\
    GradeUpdate

class SgpaInline(admin.TabularInline):
    model = Sgpa


class OtherExamPerformanceInline(admin.TabularInline):
    model = OtherExamPerformance
    

class FamilyDetailInline(admin.TabularInline):
    model = FamilyDetail    

    
class OtherScholarshipInline(admin.TabularInline):
    model = OtherScholarship

        
class ScholarshipApplicationAdmin(admin.ModelAdmin):
    fieldsets = [("Personal Details", {"fields":(('person','status',),('get_first_name','date_of_birth','sex',),
                                                 ('roll_num','get_batch','get_branch'),),}),
                 ("Contact Details", {"fields" : (('hostel_address','get_permanent_address',),
                                                  ('get_email_address', 'get_contact_number', 'parent_contact'), )}), 
                 ("SSC Details", {"fields" : (('ssc_board', 'ssc_batch', 'ssc_percentage'), 
                                              ('ssc_school_name','ssc_school_type',), 'ssc_school_address')}),
                 ("Intermediate Details", {"fields" : (('intermediate_board', 'intermediate_batch', 'intermediate_percentage'), 
                                                       ('intermediate_college_name','intermediate_college_type',), 
                                                       'intermediate_college_address')}), 
                 ("AIEEE", {"fields" : ('aieee_air',)}),
                 ("Vehicle Details", {"fields" : (('has_two_wheeler','has_four_wheeler'),)}),
                 ("House Applicances", {"fields" : (('has_tv', 'has_fridge', 'has_washing_machine'), 
                                                    ('house_ownership', 'house_type', 'agriculture_land'),'other_asset',)}),
                 ("Other questions", {"fields" : ('question1', 'question2',),}),]
    raw_id_fields = ('person', )
    readonly_fields = ('get_first_name','get_batch', 'get_branch', 'get_permanent_address', 'get_email_address', 
                       'get_contact_number',)
    list_display = ('id', 'get_first_name', 'year_of_submission', 'status')
    list_filter = ('year_of_submission', 'status',)
    search_fields = ('person__user__first_name', 'person__user__last_name')
    inlines = (SgpaInline, OtherExamPerformanceInline, FamilyDetailInline, OtherScholarshipInline)
    
class ScholarUpdateInline(admin.TabularInline):
    model = ScholarUpdate
    
class ScholarAcademicUpdateInline(admin.TabularInline):
    model = ScholarAcademicUpdate
    fields = ('get_link', 'semester', 'sgpa', 'cgpa', 'comments',)
    readonly_fields = ('get_link', 'semester', 'sgpa', 'cgpa', 'comments',)
    extra = 0
    can_delete = False

class ScholarAdmin(admin.ModelAdmin):
    raw_id_fields = ('person', 'application', 'donation_fund')
    list_display = ('id', 'person', 'donation_fund')
    list_filter = ('donation_fund',)
    search_fields = ('person__user__first_name',)
    inlines = (ScholarUpdateInline, ScholarAcademicUpdateInline)
    
class RepaymentAdmin(admin.ModelAdmin):
    raw_id_fields = ('scholar',)
    list_display = ('scholar', 'amount', 'date_of_repayment')
    list_filter = ('scholar',)
    search_fields = ('scholar__person__user__first_name', 'scholar__person__user__last_name', )
    date_hierarchy = 'date_of_repayment'

class ScholarshipPaymentAdmin(admin.ModelAdmin):
    raw_id_fields = ('scholar', 'expense',)
    list_display = ('scholar', 'amount', 'semester', )
    list_filter = ('scholar',)
    search_fields = ('scholar__person__user__first_name', 'scholar__person__user__last_name', )
    
class ScholarshipVerificationAdmin(admin.ModelAdmin):
    fieldsets = [("Volunteer Details", {"fields" : (('verifier','get_verifier_name',),
                                                    ('get_verifier_mobile_num','get_verifier_email','status',),)}),
                 ("Applicant Details", {"fields" : (('application','get_applicant_name', 'date_of_verfication',),)}),
                 ("Whom all you have interacted with", {"fields" : (('met_applicant','met_father', 'met_mother',),
                                                                    ('met_siblings','met_relatives', 'met_neighbours',),)}),
                 ("Asset Details", {"fields" : (('house_ownership_type','house_type', ),'vehicles_owned',)}),
                 ("Electronic appliances in the house", {"fields" : (('has_tv','has_fridge', 'has_washing_machine',),
                                                                     ('has_air_cooler','has_air_conditioner',))}),
                 ("Financial Details", {"fields" : ('father_details','mother_details', 'sibling_details','question1', 'question2',)}),
                 ("Is applicant aware of the rules", {"fields" : ('aware_repayment_model','aware_renewal_criteria', )}),
                 ("Summary", {"fields" : ('final_recommendation','additional_comment', )}),]
    
    readonly_fields = ('get_verifier_name', 'get_verifier_mobile_num','get_verifier_email', 
                       'get_applicant_name', )
    
    raw_id_fields = ('verifier', 'application',)
    
    list_display = ('application', "verifier", "status", "final_recommendation")
    
    list_filter = ('status', 'final_recommendation')
    
    search_fields = ('verifier__user__first_name', 'verifier__user__last_name', 
                     'applicaiton__person__user__first_name', 'application__person__user__last_name',)
    
class GradeUpdateInline(admin.TabularInline):
    model = GradeUpdate
    
class ScholarAcademicUpdateAdmin(admin.ModelAdmin):
    raw_id_fields = ('scholar',)
    inlines = (GradeUpdateInline, )
    list_display = ('scholar', 'semester', 'sgpa', 'cgpa')
    list_filter = ('semester', 'scholar',)
    search_fields = ('scholar__person__user__first_name', 'scholar__person__user__last_name',)
    
admin.site.register(ScholarshipApplication, ScholarshipApplicationAdmin)
admin.site.register(ScholarshipVerification, ScholarshipVerificationAdmin)
admin.site.register(Scholar, ScholarAdmin)
admin.site.register(ScholarshipPayment, ScholarshipPaymentAdmin)
admin.site.register(Repayment, RepaymentAdmin)
admin.site.register(ScholarAcademicUpdate, ScholarAcademicUpdateAdmin)