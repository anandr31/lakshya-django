from django.contrib import admin
from scholarships.models import ScholarshipApplication, ScholarshipVerification,\
    Scholar, ScholarshipPayment, Repayment

class ScholarshipApplicationAdmin(admin.ModelAdmin):
    fieldsets = [("Personal Details", {"fields":(('person','get_first_name',),('date_of_birth','sex',),
                                                 ('roll_num','get_batch','get_branch'),),}),
                 ("Contact Details", {"fields" : (('hostel_address','get_permanent_address',),
                                                  ('get_email_address', 'get_contact_number', 'parent_contact'), )}), 
                 ("SSC Details", {"fields" : (('ssc_board', 'ssc_batch', 'ssc_percentage'), 
                                              ('ssc_school_name','ssc_school_type',), 'ssc_school_address')}),
                 ("Intermediate Details", {"fields" : (('intermediate_board', 'intermediate_batch', 'intermediate_percentage'), 
                                                       ('intermediate_college_name','intermediate_college_type',), 
                                                       'intermediate_college_address')}), 
                 ("AIEEE", {"fields" : ('aieee_air',)}),]
    raw_id_fields = ('person', )
    readonly_fields = ('get_first_name','get_batch', 'get_branch', 'get_permanent_address', 'get_email_address', 
                       'get_contact_number',)

admin.site.register(ScholarshipApplication, ScholarshipApplicationAdmin)
admin.site.register(ScholarshipVerification)
admin.site.register(Scholar)
admin.site.register(ScholarshipPayment)
admin.site.register(Repayment)