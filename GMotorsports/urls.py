from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='GMotorsports-home'),
    path('competition/', views.competition, name='competition'),
    path('cars/', views.cars, name='cars'),
    path('team/', views.team, name='team'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('join/', views.join, name='join'),
    path('social/', views.social, name='social'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('electrical/', views.electrical, name='electrical'),
    path('aerodynamics/', views.aerodynamics, name='aerodynamics'),
    path('engine/', views.engine, name='engine'),
    path('framesuspension/', views.frame_suspension, name='frame_suspension'),
    path('externalrelations/', views.external_relations, name='external_relations'),
    path('ergonomics/', views.ergonomics, name='ergonomics'),
    path(r'^', include('cms.urls')),
]