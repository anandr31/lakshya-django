'''
Created on 26-Jul-2013

@author: srihari
'''

def modified(x):
    if not x:
        return ""
    return str(x)
    
from people.models import Person
from entrepreneurship.models import Company, FounderDetail


company_list = Company.objects.all()

for company in company_list: 
    if len(FounderDetail.objects.filter(company=company)):
        founder_detail = FounderDetail.objects.filter(company=company)[0]
        name = founder_detail.person.name()
        branch = founder_detail.person.get_department_display()
        yop = founder_detail.person.year_of_passing
        linked_in_profile = founder_detail.linkedin_link
        designation = founder_detail.designation 
        company_name = company.name
        website_url = company.website_url
        contact_number = company.contact_number
        contact_email = company.contact_email
        city = company.city
        state = company.state
        country = company.country
    else:
        name = ""
        branch = ""
        yop = ""
        linked_in_profile = ""
        designation = ""
        company_name = company.name
        website_url = company.website_url
        contact_number = company.contact_number
        contact_email = company.contact_email        
        city = company.city
        state = company.state
        country = company.country
    output_list = [name, branch, yop, designation, company_name, website_url, linked_in_profile, contact_number, contact_email, city, state, country]
    print ",".join([modified(x) for x in output_list])
    
    



