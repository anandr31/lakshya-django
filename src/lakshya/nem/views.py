# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.conf import settings
from forms import RegistrationForm
from models import Registration, ALUMNI
from accounts.utils import get_post_object
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import CCAVenueReturnForm
from django.contrib.auth.models import User
from notification import models as notification



def show_home(request):
    context = {"nem_base_url" : "http://" + settings.SITE_URL + "/static/nem/", 
               "site_url" : "http://" + settings.SITE_URL + "/",}
    return render_to_response("nem/index.html", 
                              RequestContext(request, context))
    
def registration_success(request):
    context = {"nem_base_url" : "http://" + settings.SITE_URL + "/static/nem/", 
               "site_url" : "http://" + settings.SITE_URL + "/",}
    return render_to_response("nem/registration_success.html", 
                              RequestContext(request, context))
    
def registration_failure(request):
    context = {"nem_base_url" : "http://" + settings.SITE_URL + "/static/nem/", 
               "site_url" : "http://" + settings.SITE_URL + "/",}
    return render_to_response("nem/registration_failure.html", 
                              RequestContext(request, context))
    
def register(request):
    context = {"nem_base_url" : "http://" + settings.SITE_URL + "/static/nem/", 
               "site_url" : "http://" + settings.SITE_URL + "/",}
    if request.method == 'POST': # If the form has been submitted...
        form = RegistrationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules passes
            # Process the data in form.cleaned_data
            amount_bool = form.cleaned_data['amount']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            branch = form.cleaned_data['branch']
            batch = form.cleaned_data['batch']
            pt = Registration.objects.create(amount=amount_bool, email=email, 
                                             name=name, branch=branch, batch=batch)
            transaction_id = pt.id
            if settings.ENV == "dev":
                transaction_id = "dev-nem" + str(pt.id)
            else:
                transaction_id = "nem" + str(pt.id)
            callback_url = "http://www.thelakshyafoundation.org/nem/payment-return"
            amount = 1500 if amount_bool == ALUMNI else 500
            context = {"payment_dict" : get_post_object(callback_url, amount, email, transaction_id)}
            return render_to_response("nem/registration_payment_redirect.html", 
                              RequestContext(request, context))
    else:
        form = RegistrationForm() # An unbound form
    
    context['form'] = form

    return render(request, "nem/register.html", context)

@csrf_exempt
def return_view(request):   
#    import pdb; pdb.set_trace()
    if request.method == "POST":       
        working_key = "vsb2w5ampye1baft0hg62jlwrscw007u"
        merchant_id = "M_thelaksh_10884"
        
        form = CCAVenueReturnForm(merchant_id, working_key, request.POST)
        if not form.is_valid():
            return redirect('registration-failure')
        
       
        if form.cleaned_data['AuthDesc'] == 'N':
            return redirect('registration-failure')
        
        try:
            temp_id = request.POST.get("Order_Id")
            if settings.ENV == "dev":
                #order_id will be like dev11
                temp_id = int(request.POST.get("Order_Id").split("dev-nem")[1])
            else:
                temp_id = int(request.POST.get("Order_Id").split("nem")[1])
            registration = Registration.objects.get(id=temp_id)
        except Registration.DoesNotExist:
            print "Error: Shouldn't have come here.PaymentTemp is missing"
            return redirect("registration-success")

        
        info_user = User(first_name="Info", last_name="", 
                       email="info@thelakshyafoundation.org", id=1)
        
        participant = User(first_name=registration.name, last_name="", 
                       email=registration.email, id=2)
                
        to_users = [participant, info_user]
        
        context = {"name": request.POST.get("delivery_cust_name"),
                   "amount": request.POST.get("Amount")}
        
        notification.send(to_users, "registration_confirmation", context)
        
        return redirect("registration-success")
    else:
        return redirect('registration-failure')