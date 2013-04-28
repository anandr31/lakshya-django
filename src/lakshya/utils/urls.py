from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('utils.views',
    # Examples:
    url(r'^updates$', "get_updates", name='updates'),    
    url(r'^get-donation-details-for-analytics$', "get_donation_details_for_analytics", 
        name='get_donation_details_for_analytics'),    
    url(r'^get-donor-emails-for-campaigns$', "get_donor_emails_for_campaigns", 
        name='get_donor_emails_for_campaigns'),    
)


