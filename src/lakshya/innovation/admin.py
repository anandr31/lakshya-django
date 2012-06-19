from django.contrib import admin
from innovation.models import InnovationApplication, Innovation,\
    InnovationPayment, InnovationUpdate, InnovationUpdateImage,\
    InnovationUpdateVideo

class InnovationApplicationAdmin(admin.ModelAdmin):
    filter_horizontal = ('team_members', )
    raw_id_fields = ('reviewer', )
    list_display = ('title', 'year_of_submission', 'status',)
    list_filter = ('year_of_submission', 'status', 'reviewer', )
    
class InnovationUpdateInline(admin.TabularInline):
    model = InnovationUpdate
    fields = ('get_link', 'innovation', 'date_of_update', 'update',)
    readonly_fields = ('get_link', 'innovation', 'date_of_update', 'update',)
    extra = 0
    can_delete = False
    
class InnovationAdmin(admin.ModelAdmin):
    raw_id_fields = ('application', 'guide', )
    list_display = ('get_title', 'get_year_of_submission',)
    inlines = (InnovationUpdateInline,)
    
class InnovationPaymentAdmin(admin.ModelAdmin):
    raw_id_fields = ('innovation', 'expense',)
    list_display = ('innovation', 'amount',)
    list_filter = ('innovation', )

class InnovationUpdateImageInline(admin.TabularInline):
    model = InnovationUpdateImage

class InnovationUpdateVideoInline(admin.TabularInline):
    model = InnovationUpdateVideo

class InnovationUpdateAdmin(admin.ModelAdmin):
    raw_id_fields = ('innovation',)
    list_display = ('innovation', 'date_of_update',)
    list_filter = ('innovation', )
    inlines = (InnovationUpdateImageInline, InnovationUpdateVideoInline,)

admin.site.register(InnovationApplication, InnovationApplicationAdmin)
admin.site.register(Innovation, InnovationAdmin)
admin.site.register(InnovationPayment, InnovationPaymentAdmin)
admin.site.register(InnovationUpdate, InnovationUpdateAdmin)