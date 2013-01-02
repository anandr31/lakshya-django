from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from people.models import TeamMember

def get_team_details(request):
    team_member_list = TeamMember.objects.all()  
    team_pics = {}
    for team_member in team_member_list:
        team_pics[team_member.slug] = team_member.photo.url
    return render_to_response("team.html", 
                              RequestContext(request, {'team_member_list':team_member_list, 'team_pics':team_pics,}))# Create your views here.
