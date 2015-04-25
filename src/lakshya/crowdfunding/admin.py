from django.contrib import admin
from crowdfunding.models import Project,Pledge,Message
# Register your models here.
admin.site.register(Project)
admin.site.register(Pledge)
admin.site.register(Message)