from django.forms import ModelForm
from accounts.models import PaymentTemp
from django import forms
from .utils import calc_checksum
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_str


class PaymentTempForm(ModelForm):
    class Meta:
        model = PaymentTemp

class CCAVenueReturnForm(forms.Form):
    Order_Id = forms.CharField()
    Amount = forms.CharField()
    AuthDesc = forms.CharField()
    Checksum = forms.IntegerField()
    card_category = forms.CharField()
    
    #nb_order_no = forms.CharField()
    #nb_bid = forms.IntegerField()
    
    def clean_AuthDesc(self):
        return smart_str(self.cleaned_data['AuthDesc'], encoding='ascii')
    
    def clean_Amount(self):
        return smart_str(self.cleaned_data['Amount'], encoding='ascii')
        
    def clean(self):
        checksum = self.cleaned_data['Checksum']
        transaction_id = self.cleaned_data['Order_Id']
        amount = self.cleaned_data['Amount'] 
        auth_desc = self.cleaned_data['AuthDesc']
        
        calculated_checksum = calc_checksum(self.merchant_id, transaction_id, amount, auth_desc, self.working_key)
        
        if checksum != calculated_checksum:
            raise ValidationError("Checksums did not match")
        
        return self.cleaned_data
        
    def __init__(self, merchant_id, working_key, *args, **kwargs):
        self.merchant_id = merchant_id
        self.working_key = working_key
        
        super(CCAVenueReturnForm,self).__init__(*args, **kwargs)
        
    
    