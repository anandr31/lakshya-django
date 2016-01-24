from django.contrib import admin
from hackathon.models import Participant, ProblemStatement, Hackathon, Sponsor, Mentor
from django.http import HttpResponse

# export donation to csv
def export_participant_list(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Hackathon-ParticipantList.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Hackathon"),
        smart_str(u"Name"),
        smart_str(u"Email"),
        smart_str(u"Problem Statement"),
        smart_str(u"Team"),        
        smart_str(u"Roll No"),
        smart_str(u"Year"),
        smart_str(u"Course"),
        smart_str(u"Branch"),
        smart_str(u"Mess"),
        smart_str(u"Mobile"),
        smart_str(u"T Size"),
        smart_str(u"Gender")
        
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.hackathon),
            smart_str(obj.NAME()),
            smart_str(obj.email),
            smart_str(obj.problem.name),
            smart_str(obj.team),            
            smart_str(obj.roll_no),
            smart_str(obj.YEAR()),
            smart_str(obj.COURSE()),
            smart_str(obj.BRANCH()),
            smart_str(obj.MESS()),
            smart_str(obj.mobile),
            smart_str(obj.TEE()),
            smart_str(obj.GENDER())
        ])
    return response
export_participant_list.short_description = u"Export CSV"
#ends here#


class ParticipantAdmin(admin.ModelAdmin):
    readonly_fields=('hackathon','user')
    list_display = ('NAME', 'hackathon', 'team', 'problem', 'year', 'course', 'branch', 'email', 'mobile')
    search_fields = ('hackathon', 'team', 'user', 'email','year', 'course', 'branch')
    list_filter = ('year','hackathon',)
    actions =[export_participant_list]

    
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
