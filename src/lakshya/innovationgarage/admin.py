from django.contrib import admin
from innovationgarage.models import Project, ProjectImage, Sponsor

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fields = ('image', 'show_thumbnail')
    readonly_fields = ('show_thumbnail',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'goal', 'days_remaining')
    inlines = (ProjectImageInline,)
    search_fields = ('title',)


admin.site.register(Project, ProjectAdmin)admin.site.register(Sponsor)
admin.site.register(Sponsor)
