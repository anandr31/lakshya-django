from people.models import Person, Person_preference, TeamMember
from django.contrib import admin

class PreferenceInline(admin.TabularInline):
    model = Person_preference

class PersonOptions(admin.ModelAdmin):
    fieldsets = [(None, {"fields" : [('user', 'profile_pic'),]}), 
                 ("Billing Details", {"fields" : [('billing_address',),('billing_landmark', 'billing_city',), 
                                                  ('billing_state', 'billing_postal_code'), ('billing_country', 'contact_number'), ]}), 
                 ("Alumni Details", {"fields" : [('is_nitw_alumni',), ('course', 'department', 'year_of_passing',)]}), ]
    
    list_display = ('user', 'is_nitw_alumni', 'course', "department", "year_of_passing",)
    list_filter = ('is_nitw_alumni', 'course', "department", "year_of_passing", )
    search_fields = ('user__first_name', )
    raw_id_fields = ('user', )
    inlines = (PreferenceInline, )
    
class TeamMemberOptions(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', )
    
admin.site.register(Person, PersonOptions)
admin.site.register(TeamMember, TeamMemberOptions)
