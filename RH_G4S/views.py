from django.shortcuts import render
from .forms import Formulaire

import os
import locale
import datetime
from num2words import num2words

# Create your views here.

def accueil(request): 
    return render(request, 'accueil.html',)

def modele(request): 
    #envoi = {'formulaire_contact':formulaire_contact}
    return render(request, 'modele.html',)

def lettre(request): 
    #envoi = {'formulaire_contact':formulaire_contact}
    nom_responsable, fonction_responsable, obligation_chiffre, pret_scolaire_chiffre = "", "", "", ""
    formulaire = Formulaire(request.POST or None)

    if formulaire.is_valid():

        obligation_chiffre = str(formulaire.cleaned_data["indemnite_compensatrice"])
        pret_scolaire_chiffre = str(formulaire.cleaned_data["pret_scolaire"])

        if len(obligation_chiffre) >= 4 : 
            obligation_chiffre = chiffre(formulaire.cleaned_data["indemnite_compensatrice"])    

        if len(pret_scolaire_chiffre) >= 4 : 
            pret_scolaire_chiffre = chiffre(formulaire.cleaned_data["pret_scolaire"])

        if formulaire.cleaned_data["fonction_responsable"] == "" : 
            fonction_responsable = "La Responsable des Opérations RH"  
        else : 
            fonction_responsable = formulaire.cleaned_data["fonction_responsable"] 

        if formulaire.cleaned_data["nom_responsable"] == "" :
            nom_responsable = "Marie Danielle ACHI" 
        else : 
            nom_responsable = formulaire.cleaned_data["nom_responsable"]     

        context = {'civilite': formulaire.cleaned_data["civilite"], 'nom_prenom': formulaire.cleaned_data["nom"], 
                    'fonction': formulaire.cleaned_data["fonction"], 'matricule': formulaire.cleaned_data["matricule"], 
                    'date_embauche': str(formulaire.cleaned_data["date_embauche"].strftime("%d")) + "/" + 
                        str(formulaire.cleaned_data["date_embauche"].strftime("%m")) + "/" + 
                        str(formulaire.cleaned_data["date_embauche"].strftime("%Y")),
                    'categorie': formulaire.cleaned_data["categorie"], 'numero_cnps': formulaire.cleaned_data["numero_cnps"] , 
                    'duree_preavis': formulaire.cleaned_data["duree_de_preavis"].lower, 
                    'duree_de_preavis_en_toute_lettre' : formulaire.cleaned_data["duree_de_preavis_en_toute_lettre"].lower,
                    'obligation_lettre': majuscule(formulaire.cleaned_data["indemnite_compensatrice"]), 
                    'obligation_chiffre': obligation_chiffre, 
                    'pret_scolaire_lettre': majuscule(formulaire.cleaned_data["pret_scolaire"]), 
                    'pret_scolaire_chiffre': pret_scolaire_chiffre, 
                    'date': date_en_francais(), 'fonction_responsable': fonction_responsable, 
                    'nom_responsable': nom_responsable, 'reference_lettre':formulaire.cleaned_data["reference_lettre"]}
            
        return render(request, 'resultat.html', context)
    
    return render(request, 'lettre.html', {"formulaire": formulaire})   
  


# Gestion de la date automatique  
def set_locale(locale_):
    locale.setlocale(category=locale.LC_ALL, locale=locale_)

def date_en_francais() : 
    set_locale('fr_FR.utf8')
    
    date = datetime.datetime.now().strftime("%d %B %Y")
    entree, sortie = str(date).split(), ""
    for e in entree :
        e = e.replace(e[0], e[0].upper())  
        sortie = sortie + e + " "
    sortie = sortie[0: len(sortie) - 1]    
    return sortie

# Autres fonctions : convertir des chiffres en lettres et les mettre en majuscule
def chiffre(chiffre) :
    chiffre = str(chiffre)
    new_chiffre =""
    while len (chiffre) >= 4 : 
        droite = chiffre[-3:]
        new_chiffre = " " + droite + new_chiffre 
        gauche = chiffre[:len(chiffre) - 3]
        chiffre = gauche
    new_chiffre = gauche + new_chiffre     
    return new_chiffre    

def majuscule(lettre) :
    entree = num2words(lettre, lang="fr")
    entree = str(entree).lower()
    entree = entree.split()   
    sortie = ""
    for e in entree : 
        if e.find("-") == -1 : 
            e = e.replace(e[0], e[0].upper())  
            sortie = sortie + e + " "
        else : 
            sortie = sortie + majuscule_avec_trait(e) + " "   
    sortie = sortie[0: len(sortie) - 1]        
    return sortie    

def majuscule_avec_trait(lettre) :
    lettre = str(lettre)
    entree = lettre.lower()
    entree = entree.replace("-", " ")
    entree = entree.split()   
    sortie = ""
    for e in entree : 
        e = e.replace(e[0], e[0].upper())  
        sortie = sortie + e + "-"
    if sortie[-1] == "-" :
        sortie = sortie[0: len(sortie) - 1]    
    return sortie        