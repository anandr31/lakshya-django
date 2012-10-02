# Create your views here.
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from accounts.models import Expense, Donation
from django.db.models import Sum
from people.models import Person

def download_donation_receipt(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=donation-receipt.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def expenses_home(request):
    expenses_list = Expense.objects.all()
    context = {"expenses_list" : expenses_list}
    return render_to_response("expenses.html", 
                              RequestContext(request, context))
    
def donations_home(request):
    donor_details_list = [] #list of tuples - name, batch, branch, amount, last Donated on
    for temp_dict in Donation.objects.values('donor').annotate(total=Sum('amount')):
        donor_id = temp_dict["donor"]
        total = temp_dict["total"]
        donor = Person.objects.get(id=donor_id)
        last_donated_on = Donation.objects.filter(donor = donor).order_by("-date_of_donation")[0].date_of_donation
        donor_details = (donor.name, donor.year_of_passing, donor.get_department_display, total, last_donated_on)
        donor_details_list.append(donor_details)
    context = {"donor_details_list" : donor_details_list}
    return render_to_response("donations.html", 
                              RequestContext(request, context)) 
    
    