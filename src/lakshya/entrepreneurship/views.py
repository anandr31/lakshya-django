from django.db.models import Count
from models import Company, Sector
from django.template.context import RequestContext
from django.shortcuts import render_to_response


def companies_listing(request):
    companies = Company.objects.all()
    total_companies_count = companies.count
    sectors_count_map = [(Sector.objects.get(id=map['sectors']), map['sectors__count']) for map in \
                                             Company.objects.all().values('sectors').annotate(Count('sectors'))]
    sectors_list_details = ((x[0].name, x[0].slug, x[1]) for x in sectors_count_map)
    selected_batch = request.GET.get("batch", None)
    selected_sector = request.GET.get("sector", None)
    selected_sector_name = None
    if selected_sector:
        companies = companies.filter(sectors__slug=selected_sector)
        selected_sector_name = Sector.objects.get(slug=selected_sector).name
    if selected_batch:
        companies = companies.filter(founders__person__batch=selected_batch)        
    selected_companies_count = companies.count()
    context = {"companies" : companies, 
               "total_companies_count" : total_companies_count, 
               "sectors_list_details" : sectors_list_details, 
               "selected_batch" : selected_batch, 
               "selected_sector" : selected_sector, 
               "selected_sector_name" : selected_sector_name, 
               "selected_companies_count" : selected_companies_count}
    return render_to_response("companies_listing.html", 
                              RequestContext(request, context)) 
    
def company_detail(request, company_slug):
    sectors_count_map = [(Sector.objects.get(id=map['sectors']), map['sectors__count']) for map in \
                                             Company.objects.all().values('sectors').annotate(Count('sectors'))]
    sectors_list_details = ((x[0].name, x[0].slug, x[1]) for x in sectors_count_map)
    company = Company.objects.get(slug=company_slug) 
    context = { "sectors_list_details" : sectors_list_details, 
                "company" : company,
               }
    return render_to_response("company_detail.html", 
                              RequestContext(request, context))    
    
    
    