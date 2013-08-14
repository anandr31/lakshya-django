'''
Created on 15-Aug-2013

@author: srihari
'''
from django.contrib import admin
from models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'batch',)
    list_filter = ('batch', 'branch',)

admin.site.register(Registration, RegistrationAdmin)
