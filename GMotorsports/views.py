from django.shortcuts import render
from .models import *

def home(request):
    context = {}
    context['HomeCMS'] = HomePage.objects.first()
    return render(request, 'GMotorsports/home.html', context)

def competition(request):
    context = {}
    context['CompetitionCMS'] = CompetitionPage.objects.first()
    return render(request, 'GMotorsports/Competition.html', context)

def cars(request):
    context = {}
    context['CarsCMS'] = CarsPage.objects.first()
    return render(request, 'GMotorsports/Cars.html', context)

def team(request):
    context = {}
    context['TeamCMS'] = TeamPage.objects.first()
    return render(request, 'GMotorsports/Team.html', context)

def sponsors(request):
    return render(request, 'GMotorsports/Sponsors.html', {})

def join(request):
    context = {}
    context['JoinTeamCMS'] = JoinTeamPage.objects.first()
    return render(request, 'GMotorsports/Join The Team.html', context)

def social(request):
    return render(request, 'GMotorsports/Social.html', {})

def contact(request):
    return render(request, 'GMotorsports/Contact.html', {})

def donate(request):
    context = {}
    context['DonateCMS'] = DonatePage.objects.first()
    return render(request, 'GMotorsports/Donate.html', context)

def electrical(request):
    context = {}
    context['Electrical'] = SubteamPage.objects.filter(subteam="electrical")[0]
    return render(request, 'GMotorsports/Electrical.html', context)

def aerodynamics(request):
    context = {}
    context['Aerodynamics'] = SubteamPage.objects.filter(subteam="aerodynamics")[0]
    return render(request, 'GMotorsports/Aerodynamics.html', context)

def engine(request):
    context = {}
    context['Engine'] = SubteamPage.objects.filter(subteam="engine")[0]
    return render(request, 'GMotorsports/Engine.html', context)

def external_relations(request):
    context = {}
    context['External_relations'] = SubteamPage.objects.filter(subteam="external_relations")[0]
    return render(request, 'GMotorsports/ExternalRelations.html', context)

def frame_suspension(request):
    context = {}
    context['Frame_suspension'] = SubteamPage.objects.filter(subteam="frame_suspension")[0]
    return render(request, 'GMotorsports/FrameSuspension.html', context)

def ergonomics(request):
    context = {}
    context['Ergonomics'] = SubteamPage.objects.filter(subteam="ergonomics")[0]
    return render(request, 'GMotorsports/Ergonomics.html', context)