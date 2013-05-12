from django.contrib import admin
from models import Sector, Company, FounderDetail


class FounderInline(admin.StackedInline):
    model = FounderDetail   
    extra = 1
    
class CompanyAdmin(admin.ModelAdmin):
    filter_horizontal = ('sectors',)
    inlines = (FounderInline, )

admin.site.register(Sector)
admin.site.register(Company, CompanyAdmin)
