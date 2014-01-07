from django.contrib import admin
from utils.models import LakshyaUpdate, LakshyaTestimonial

class LakshyaUpdateOptions(admin.ModelAdmin):
    list_display = ('update_text', 'date_of_entry', 'sorting', "active",)
    list_editable = ('sorting', )
    list_filter = ('active', )
    search_fields = ('update_text', )
    
class LakshyaTestimonialOptions(admin.ModelAdmin):
    list_display = ('person', 'date_of_entry', "sorting", "active")
    list_filter = ('active', )
    search_fields = ('testimonial_text', 'person__name',)
    raw_id_fields = ('person', )    
    
admin.site.register(LakshyaUpdate, LakshyaUpdateOptions)
admin.site.register(LakshyaTestimonial, LakshyaTestimonialOptions)
