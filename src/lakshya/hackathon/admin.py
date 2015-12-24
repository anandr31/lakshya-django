from django.contrib import admin

from hackathon.models import Participant, ProblemStatement, Hackathon, Sponsor, Mentor


class ParticipantAdmin(admin.ModelAdmin):
    readonly_fields=('hackathon','user')
    list_display = ('user', 'hackathon', 'year', 'course', 'branch', 'email', 'mobile')
    search_fields = ('hackathon', 'user', 'email','year', 'course', 'branch')
    list_filter = ('year','hackathon',)
    
class ProblemStatementAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_link', 'hackathon')
    search_fields = ('name', 'add_link', 'hackathon__name')
    list_filter = ('hackathon',)


class HackathonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_active')
    search_fields = ('name',)


class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'hackathon',)
    search_fields = ('name', 'website',)


class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hackathon',)
    search_fields = ('name',)
    raw_id_fields = ('hackathon',)

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(ProblemStatement, ProblemStatementAdmin)
admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Sponsor, SponsorsAdmin)
admin.site.register(Mentor, MentorAdmin)
