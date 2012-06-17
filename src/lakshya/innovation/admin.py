from django.contrib import admin
from innovation.models import InnovationApplication, Innovation,\
    InnovationPayment

admin.site.register(InnovationApplication)
admin.site.register(Innovation)
admin.site.register(InnovationPayment)