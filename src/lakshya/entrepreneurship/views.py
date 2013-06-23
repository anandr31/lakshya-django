from django.db.models import Count
from models import Company, Sector, CompanyAttribute, FounderDetail
from django.template.context import RequestContext
from django.shortcuts import render_to_response


def companies_listing(request):
    companies = Company.objects.all()
    total_companies_count = companies.count
    
    #By Sectors
    sectors_count_map = []
    for sector_map in Company.objects.all().values('sectors').annotate(Count('sectors')):
        if len(Sector.objects.filter(id=sector_map['sectors'])):
            sectors_count_map.append((Sector.objects.get(id=sector_map['sectors']), sector_map['sectors__count']))
    sectors_list_details = ((x[0].name, x[0].slug, x[1]) for x in sectors_count_map)
    
    #By Batch
    
    #By Country
    countries_list_details = [(map['country'], map['country__count']) for map in \
                                             Company.objects.all().values('country').annotate(Count('country'))]
        
    selected_batch = request.GET.get("batch", None)
    selected_sector = request.GET.get("sector", None)
    selected_country = request.GET.get("country", None)
    selected_sector_name = None
    if selected_sector:
        companies = companies.filter(sectors__slug=selected_sector)
        selected_sector_name = Sector.objects.get(slug=selected_sector).name
    if selected_batch:
        companies = companies.filter(founders__person__batch=selected_batch)   
    if selected_country:
        companies = companies.filter(country=selected_country) 
             
    selected_companies_count = companies.count()
    context = {"companies" : companies, 
               "total_companies_count" : total_companies_count, 
               "sectors_list_details" : sectors_list_details, 
               "selected_batch" : selected_batch, 
               "selected_sector" : selected_sector, 
               "selected_sector_name" : selected_sector_name, 
               "selected_companies_count" : selected_companies_count,
               "countries_list_details" : countries_list_details, 
               "selected_country" : selected_country, }
    return render_to_response("companies_listing.html", 
                              RequestContext(request, context)) 
    
def company_detail(request, company_slug):
    total_companies_count = Company.objects.all().count
    sectors_count_map = [(Sector.objects.get(id=map['sectors']), map['sectors__count']) for map in \
                                             Company.objects.all().values('sectors').annotate(Count('sectors'))]
    sectors_list_details = ((x[0].name, x[0].slug, x[1]) for x in sectors_count_map)
    
    countries_list_details = [(map['country'], map['country__count']) for map in \
                                             Company.objects.all().values('country').annotate(Count('country'))]
        
    company = Company.objects.get(slug=company_slug) 
    company_attributes = CompanyAttribute.objects.filter(company=company).order_by("option__ordering")
    founder_details = FounderDetail.objects.filter(company=company)
    sectors_name_list = ", ".join([x.name for x in company.sectors.all()])
    other_companies_in_sector = Company.objects.filter(sectors__in = company.sectors.all()).distinct().exclude(id=company.id)  
    context = { "sectors_list_details" : sectors_list_details, 
                "company" : company,
                "company_attributes" : company_attributes,
                "founder_details" : founder_details,
                "sectors_name_list" : sectors_name_list,
                "other_companies_in_sector" : other_companies_in_sector,
                "countries_list_details" : countries_list_details,
                "total_companies_count" : total_companies_count,
               }
    return render_to_response("company_detail.html", 
                              RequestContext(request, context))    
    
    
    