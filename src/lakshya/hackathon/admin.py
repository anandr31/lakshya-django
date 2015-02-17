from django.contrib import admin

from hackathon.models import Participant, ProblemStatement, Hackathon, Sponsors, Contact, Mentor


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'YEAR', 'COURSE', 'BRANCH', 'email', 'mobile')
    search_fields = ('name', 'email',)
    list_filter = ('year',)


class ProblemStatementAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_link', 'hackathon')
    search_fields = ('name', 'add_link', 'hackathon__name')


class HackathonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_active')
    search_fields = ('name',)


class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'hackathon',)
    search_fields = ('name', 'url',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'contact_info', 'type', 'created')
    search_fields = ('name', 'contact_info', 'company')
    list_filter = ('type',)


class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hackathon',)
    search_fields = ('name',)
    raw_id_fields = ('hackathon',)

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(ProblemStatement, ProblemStatementAdmin)
admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Mentor, MentorAdmin)
