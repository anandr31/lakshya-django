from django.shortcuts import render
from forms import RegistrationForm
from models import *

# Create your views here.

def index(request):
    return render(request, 'hackathon/index.html', {})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form.save()

        return render(request,"hackathon/success.html",{})
    else:
        form = RegistrationForm()
        return render(request,'project/register.html',{'form':form})