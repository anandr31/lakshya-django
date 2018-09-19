from zlib import adler32

from django.conf import settings

from people.models import Person

def calc_checksum(*args):
    '''
    Calculates the check sum of the given args
    '''
    checksum_string = "|".join(map(str,args))
    return adler32(checksum_string, 1) & 0xffffffff

def get_post_object(callback_url, amount, email_address, transaction_id, notes):
    try:
        donor = Person.objects.get(user__email=email_address)
        name = donor.name
        address = donor.billing_address
        country = donor.billing_country
        contact_number = donor.contact_number
        email = email_address
        state = donor.billing_state
        city = donor.billing_city
        zip_code = donor.billing_postal_code

        return {
            "Merchant_Id" :settings.CCAVENUE_MERCHANT_ID ,
            "Amount" :amount ,
            "Order_Id" :transaction_id ,
            "Redirect_Url" :callback_url ,

            "Checksum" :calc_checksum(settings.CCAVENUE_MERCHANT_ID, transaction_id, amount, callback_url, settings.CCAVENUE_WORKING_KEY) ,

            "billing_cust_name" :name ,
            "billing_cust_address" :address ,
            "billing_cust_country" :country ,
            "billing_cust_tel" :contact_number ,
            "billing_cust_email" :email ,
            "billing_cust_state" :state ,
            "billing_cust_city" :city ,
            "billing_zip_code" :zip_code ,
            "billing_cust_notes" :notes,
            "delivery_cust_name" :name ,
            "delivery_cust_address" :address ,
            "delivery_cust_country" :country ,
            "delivery_cust_state" :state ,
            "delivery_cust_city" :city ,
            "delivery_cust_tel" :contact_number ,
            "delivery_zip_code" :zip_code ,
        }
    except:
        return {
            "Merchant_Id" :settings.CCAVENUE_MERCHANT_ID ,
            "Amount" :amount ,
            "Order_Id" :transaction_id ,
            "Redirect_Url" :callback_url ,
            "Checksum" :calc_checksum(settings.CCAVENUE_MERCHANT_ID, transaction_id, amount, callback_url, settings.CCAVENUE_WORKING_KEY) ,
            "billing_cust_name" :"" ,
            "billing_cust_address" :"" ,
            "billing_cust_country" :"" ,
            "billing_cust_tel" :"" ,
            "billing_cust_email" :email_address ,
            "billing_cust_state" :"" ,
            "billing_cust_city" :"" ,
            "billing_zip" :"" ,
            "billing_cust_notes" :notes,
            "delivery_cust_name" :"" ,
            "delivery_cust_address" :"" ,
            "delivery_cust_country" :"" ,
            "delivery_cust_state" :"" ,
            "delivery_cust_city" :"" ,
            "delivery_cust_tel" :"" ,
            "delivery_zip_code" :"" ,
            "billing_zip_code" : "",
            "Merchant_Param" : "",
        }
