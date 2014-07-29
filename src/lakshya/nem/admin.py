'''
Created on 15-Aug-2013

@author: srihari
'''
from django.contrib import admin
from models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'batch','status')
    list_filter = ('batch', 'branch', 'status')

admin.site.register(Registration, RegistrationAdmin)
