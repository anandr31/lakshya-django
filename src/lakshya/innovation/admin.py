from django.contrib import admin
from innovation.models import IspApplication, Innovation, \
    InnovationPayment, InnovationUpdate, InnovationUpdateImage, \
    InnovationUpdateVideo, ACCEPTED, InnovationInstrument
from django import forms


class IspApplicationAdmin(admin.ModelAdmin):
    fieldsets = [("Basic Details", {"fields": [('date_of_submission', 'status',), ]}),
                 ("Project Details", {"fields": ['title', 'abstract', "expected_expenditure"]}),
                 ("Team Details", {"fields": ['get_member_detail', 'member', 'other_member_details', ]}),
                 ("Review Details", {"fields": ['review', ]}), ]
    raw_id_fields = ('member',)
    list_display = ('title', 'year_of_submission', 'status',)
    list_filter = ('year_of_submission', 'status',)
    readonly_fields = ("get_member_detail", "date_of_submission",)


class InnovationUpdateInline(admin.TabularInline):
    model = InnovationUpdate
    fields = ('get_link', 'innovation', 'date_of_update', 'update',)
    readonly_fields = ('get_link', 'innovation', 'date_of_update', 'update',)
    extra = 0
    can_delete = False
    max_num = 0


class InnovationAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        application = self.cleaned_data['application']

        if application and application.status != ACCEPTED:
            self._errors["application"] = self.error_class(["You can only select innovation applications" +
                                                            " in 'Accepted' status"])
            del cleaned_data["application"]
        return cleaned_data

    class Meta:
        model = Innovation


class InnovationAdmin(admin.ModelAdmin):
    raw_id_fields = ('application', 'guide',)
    list_display = ('get_title', 'get_year_of_submission',)
    inlines = (InnovationUpdateInline,)
    form = InnovationAdminForm


class InnovationPaymentAdmin(admin.ModelAdmin):
    raw_id_fields = ('innovation', 'expense',)
    list_display = ('innovation', 'amount',)
    list_filter = ('innovation',)
    readonly_fields = ('amount',)


class InnovationUpdateImageInline(admin.TabularInline):
    model = InnovationUpdateImage


class InnovationUpdateVideoInline(admin.TabularInline):
    model = InnovationUpdateVideo


class InnovationUpdateAdmin(admin.ModelAdmin):
    raw_id_fields = ('innovation',)
    list_display = ('innovation', 'date_of_update',)
    list_filter = ('innovation',)
    inlines = (InnovationUpdateImageInline, InnovationUpdateVideoInline,)


class InnovationInstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created')
    search_fields = ('name',)


admin.site.register(IspApplication, IspApplicationAdmin)
admin.site.register(Innovation, InnovationAdmin)
admin.site.register(InnovationPayment, InnovationPaymentAdmin)
admin.site.register(InnovationUpdate, InnovationUpdateAdmin)
admin.site.register(InnovationInstrument, InnovationInstrumentAdmin)
