from django.urls import path
from . import views
#from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView  

app_name = 'RH_G4S'

urlpatterns = [

    # Accueil
    path('', views.accueil, name='accueil'),  

    # Modèle
    path('modele', views.modele, name='modele'),
    path('modele_PS_rembourse', views.modele_PS_rembourse, name='modele_PS_rembourse'),
    path('modele_PS_non_rembourse', views.modele_PS_non_rembourse, name='modele_PS_non_rembourse'),  
    path('modele_sans_PS', views.modele_sans_PS, name='modele_sans_PS'), 

    # Lettre
    path('lettre', views.lettre, name='lettre'),
    path('lettre_sans_PS', views.lettre_sans_PS, name='lettre_sans_PS'),
    path('lettre_avec_PS', views.lettre_avec_PS, name='lettre_avec_PS'), 
    path('lettre_PS_rembourse', views.lettre_PS_rembourse, name='lettre_PS_rembourse'),

    # Contact 
    path('contact', views.contact, name='contact'),

    ]