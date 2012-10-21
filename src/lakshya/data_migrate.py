from accounts.models import *
from people.models import *
from itertools import islice
from django.contrib.auth.models import *
import datetime
import pprint


def get_branch(s):
    branch = get_value(s)
    branch_id_map = {
        "ECE":0,
        "EEE":1,
        "CSE":2,
        "Mechanical":3,
        "Civil":4,
        "Chemical":5,
        "Metallurgy":6,
        "Biotech":7,                     
    }
    
    if branch:
        return branch_id_map[branch]
    else:
        return 0

def get_mode(s):
    mode = get_value(s)
    mode_id_map = {
        "CHEQUE/DD":2,
        "CASH":4,
        "ONLINE":5,
        "CC AVENUE":1,                    
    }
    
    if mode:
        return mode_id_map[mode.upper()]
    else:
        return 0

def get_value(s):
    return s[s.find(":")+1:].strip()

def load_data():
    address_list = {}
    print "-------- lakshya account -------------"
    with open("/home/srihari/Desktop/data-migration-final/lakshya_account") as f:
        while True:
            next_n_lines = list(islice(f, 13))
            if not next_n_lines:
                break
            else:
                acc_id = int(get_value(next_n_lines[1])) + 25
                username = get_value(next_n_lines[2])
                email = get_value(next_n_lines[4])
                name = get_value(next_n_lines[6])
                addr = get_value(next_n_lines[7])
                city= get_value(next_n_lines[8])
                province= get_value(next_n_lines[9])
                zipcode= get_value(next_n_lines[10])
                country= get_value(next_n_lines[11])
                mobile= get_value(next_n_lines[12])
                  
                acc = User(id= acc_id, username=username, first_name=name, email=email, password="lakshya123") 
                acc.save()
                address_list[acc_id] = {"addr" : addr,
                                    "city" : city,
                                    "province" : province,
                                    "zipcode" : zipcode,     
                                    "country" :  country,
                                    "mobile" : mobile,                            
                                    }
                

    print "-------- lakshya donor -------------"    
    with open("/home/srihari/Desktop/data-migration-final/lakshya_donor") as f:
        while True:
            next_n_lines = list(islice(f, 10))
            if not next_n_lines:
                break
            else:        
                person_id = int(get_value(next_n_lines[1])) + 25
                user_id = int(get_value(next_n_lines[2])) + 25
                is_nitw_alumni = 1 if get_value(next_n_lines[3]) == "NITW" else 0
                branch = get_branch(next_n_lines[4])
                yop = int(get_value(next_n_lines[5])) if get_value(next_n_lines[5]) else 0
                address_dict = address_list[user_id]
                person = Person(id = person_id, 
                                user_id = user_id,
                                billing_address = address_dict["addr"], 
                                billing_city = address_dict["city"],
                                billing_state = address_dict["province"],
                                billing_postal_code = address_dict["zipcode"],
                                billing_country = address_dict["country"],
                                contact_number = address_dict["mobile"],
                                is_nitw_alumni = is_nitw_alumni,
                                department = branch,
                                year_of_passing = yop,
                                )
                try:
                    Person.objects.get(id = person_id)
                except:
                    person.save()
                
    print "-------- lakshya donation -------------"  
    with open("/home/srihari/Desktop/data-migration-final/lakshya_donation") as f:
        while True:
            next_n_lines = list(islice(f, 9))
            if not next_n_lines:
                break
            else: 
                donation_id = int(get_value(next_n_lines[1]))
                donor_id = int(get_value(next_n_lines[2])) + 25
                amount = int(get_value(next_n_lines[3]))
                donDate = datetime.datetime.strptime(get_value(next_n_lines[4]), "%Y-%m-%d").date()
                donMode = get_mode(next_n_lines[5])
                donDetails = get_value(next_n_lines[6])

                donation = Donation(id = donation_id, 
                                     amount = amount, 
                                     date_of_donation = donDate, 
                                     donor_id = donor_id,
                                     donation_fund_id = 11,
                                     transacation_type = donMode,
                                     transaction_details = donDetails)
                try:
                    Donation.objects.get(id = donation_id)
                except:
                    donation.save()
#                print pprint.pprint(vars(donation))
