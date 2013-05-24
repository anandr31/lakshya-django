from django.contrib import admin
from models import Sector, Company, FounderDetail, CompanyAttribute, CompanyPhoto, AttributeOption

class CompanyAttributeInline(admin.TabularInline):
    model = CompanyAttribute   
    extra = 3    

class FounderInline(admin.StackedInline):
    model = FounderDetail   
    extra = 1
    
class CompanyPhotoInline(admin.TabularInline):
    model = CompanyPhoto   
    extra = 3     
    
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields" : [('name', 'slug'), "description", "sectors", ("website_url", "video_url"), "logo", ]}),
                 ("Address", {"fields" : [('city', 'postal_code',),('state', 'country',),],}),
                 ("Contact Information", {"fields" : [('contact_number', 'contact_email',),]}),]
    filter_horizontal = ('sectors',)
    inlines = (CompanyAttributeInline, CompanyPhotoInline, FounderInline, )

admin.site.register(Sector)
admin.site.register(AttributeOption)
admin.site.register(Company, CompanyAdmin)
