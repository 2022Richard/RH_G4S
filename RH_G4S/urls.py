from django.urls import path
from . import views
#from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView  

app_name = 'RH_G4S'

urlpatterns = [

    path('', views.accueil, name='accueil'),  
    path('modele', views.modele, name='modele'),  
    path('lettre', views.lettre, name='lettre'),  
    ]