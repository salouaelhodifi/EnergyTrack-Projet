"""
URL configuration for EnergyTrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('actualites/', views.actualites, name='actualites'),
    path('about/', views.about, name='about'),
    path('actualites/bloc1/', views.bloc1, name='bloc1'),
    path('actualites/bloc2/', views.bloc2, name='bloc2'),
    path('actualites/bloc3/', views.bloc3, name='bloc3'),
    path('actualites/bloc4/', views.bloc4, name='bloc4'),
    path('actualites/bloc5/', views.bloc5, name='bloc5'),
    path('actualites/bloc6/', views.bloc6, name='bloc6'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('docutheque/', views.docutheque, name='docutheque'),
    path('world/', views.world, name='world'),
    path('solar/', views.solar, name='solar'),
    path('wind/', views.wind, name='wind'),
    path('fossile/', views.fossile, name='fossile'),
    path('renouvelable/', views.renouvelable, name='renouvelable'),
    path('petrole/', views.petrole, name='petrole'),
    path('nucleaire/', views.nucleaire, name='nucleaire'),
    path('hydraulique/', views.hydraulique, name='hydraulique'),
    path('gaz/', views.gaz, name='gaz'),
    path('charbon/', views.charbon, name='charbon'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('consommation/', views.consommation, name='consommation'),
    path('newslater/', views.newslater, name='newslater'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('payment/', views.payment, name='payment'),
    path('confirmation/', views.confirmation, name='confirmation'),
     path('payment./', views.payment1, name='payment'),
    path('confirmation./', views.confirmation1, name='confirmation'),
     path('paiement/', views.paiement, name='paiement'),

    
]


