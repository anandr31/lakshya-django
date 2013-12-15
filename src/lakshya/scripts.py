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
from openpyxl.reader.excel import load_workbook
import datetime
from accounts.models import *
from scholarships.models import *



def companu_list():
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
    

def update_expenses(path):
    wb = load_workbook(filename = path)
    ws = wb.get_active_sheet()
    for i in range(0, len(ws.columns[0])):
    # for i in range(0, 1):
        if str(ws.columns[4][i].value) == 'Approved':
            amount = int(ws.columns[0][i].value)
            date = ws.columns[1][i].value
            project = 1
            header = 2
            status = 1
            scholar = Scholar.objects.all()[0]
            try:
                scholar = Scholar.objects.get(person__id = int(ws.columns[7][i].value))
            except:
                pass
            if ws.columns[8][i].value == "Mess":
                payment_reason = 3
            elif ws.columns[8][i].value == "Laptop":
                payment_reason = 4
            else:
                payment_reason = 1
            transaction_number = ws.columns[9][i].value
            if ws.columns[10][i].value == 'Y':
                payment_type = 0
            else:
                payment_type = 1
            details = ws.columns[11][i].value or "Not yet added"
            exp = Expense.objects.create(amount=amount, date_of_expense=date, status=status, expense_header_first_level=project,
                expense_header_second_level=header, details=details, payment_type=payment_type, transaction_number=transaction_number)
            print exp
            sp = ScholarshipPayment.objects.create(scholar=scholar, amount=amount, semester=1, payment_reason=payment_reason, expense=exp)
            print sp



