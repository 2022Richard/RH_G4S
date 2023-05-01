from django import forms

from django.urls import reverse_lazy
from datetime import datetime
from django.core.exceptions import ValidationError
#from django.db import models


#Crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
#J'ai besoin de : Layout, Submit, Row, Column, Fieldset, ButtonHolder, HTML, Field, InlineRadios 
from crispy_forms.bootstrap import FormActions, InlineRadios, InlineCheckboxes


class Formulaire(forms.Form):
    
    liste_1 = (("Monsieur", "Monsieur"), ("Madame","Madame"), ("Mademoiselle", "Mademoiselle"))
    liste_2 = (("1ere", "1ere"), ("2e","2e" ), ("3e","3e" ), ("4e","4e" ), ("5e","5e" ), ("6e","6e" ), 
                ("7e","7e" ), ("8e","8e" ), ("9e","9e" ), ("10e","10e" ))

    civilite = forms.ChoiceField(label ='Civilite' ,required=False ,choices=liste_1,)

    date_reception_courrier= forms.DateField(label = 'Date de reception du courrier de démission' ,required=True , widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date, 'required':''}))

    nom = forms.CharField(label ='Nom(s) et Prénom(s)',required=True ,widget=forms.TextInput(attrs={'placeholder': 
        'Entrer le nom et le prénom ','required':''}))

    fonction = forms.CharField(label ='Fonction',required=True ,widget=forms.TextInput(attrs={'placeholder': 
        'Entrer la fonction ','required':''}))
    matricule = forms.IntegerField(label ='Matricule',min_value = 1, required=True,)

    date_embauche = forms.DateField(required=True , widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date, 'required':''}))
    categorie = forms.ChoiceField(label ='Categorie' ,required=False ,choices=liste_2,)
    
    numero_cnps = forms.IntegerField(label ='Numéro CNPS',min_value = 1, required=True,)

    duree_de_preavis = forms.CharField(label ='Durée préavis',required=True ,widget=forms.TextInput(attrs={'placeholder': 
        'Exemple: trois (03) mois ','required':''}))

    duree_de_preavis_en_toute_lettre = forms.CharField(label ='Durée préavis',required=True ,widget=forms.TextInput(attrs={'placeholder':
        'Exemple: du 01 janvier 2023 au 01 avril 2023','required':''}))

    indemnite_compensatrice = forms.IntegerField(label ='Montant de l\'indémité compensatrice du préavis',min_value = 1, required=True,)
    pret_scolaire = forms.IntegerField(label ='Montant du prêt scolaire',min_value = 1, required=True,)
     
    fonction_responsable = forms.CharField(label ='Fonction du Responsable RH', 
    required=False ,widget=forms.TextInput(attrs={'placeholder':'Par Défaut : La Responsable des Opérations RH',}))

    nom_responsable = forms.CharField(label ='Nom du Responsable RH', 
    required=False ,widget=forms.TextInput(attrs={'placeholder': 'Par Défaut : Marie Danielle ACHI ',}))  

    reference_lettre = forms.CharField(label ='Référence de la lettre',required=True ,widget=forms.TextInput(attrs={'placeholder': 
        'Exemple : DRHF/MDA/MC/11-22','required':''}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        #self.helper.form_action = reverse_lazy("RH_G4S:modele")

        self.helper.layout = Layout(
             Row(               
                Column('date_reception_courrier'),
                Column('civilite'),
                Column('nom'),
                ),
            Row(
                
                Column('fonction'),
                Column('matricule'),
                Column('date_embauche'),
                ),    
            Row(
                Column('categorie'),
                Column('numero_cnps'),  
                Column('duree_de_preavis'),        
                ),
            Row(    
                Column('duree_de_preavis_en_toute_lettre'),
                Column('indemnite_compensatrice'),
                Column('pret_scolaire'),
                ),    
                  
            Row(
                Column('nom_responsable', css_class="rows=10"),
                Column('fonction_responsable', css_class="rows=10"),
                Column('reference_lettre'),
                
               ),
            Submit('submit', 'Envoyer', css_class="btn btn-primary w-100 m-0")
        )


class form_sans_PS(Formulaire):
    #pret_scolaire = forms.HiddenInput()
    pret_scolaire = forms.IntegerField(required=False ,widget= forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        # self.helper.form_action = reverse_lazy("RH_G4S:modele")

        self.helper.layout = Layout(
             Row(               
                Column('date_reception_courrier'),
               
                Column('civilite'),
                ),
            Row(
                Column('nom'),
                Column('fonction'),
                Column('matricule'),
                ),    
            Row(
                Column('date_embauche'),
                Column('categorie'),
                Column('numero_cnps'),              
                ),
            Row(
                Column('duree_de_preavis'),
                Column('duree_de_preavis_en_toute_lettre'),
                Column('indemnite_compensatrice'),
                ),    
                  
            Row(
                Column('nom_responsable', css_class="rows=10"),
                Column('fonction_responsable', css_class="rows=10"),
                Column('reference_lettre'),
               ),
            Submit('submit', 'Envoyer', css_class="btn btn-primary w-100 m-0")
        )

class form_rembourse(Formulaire):
    remboursement_PS = forms.IntegerField(label ='Montant restant après le remboursement du PS',min_value = 1, required=True,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        #self.helper.form_action = reverse_lazy("RH_G4S:modele")

        self.helper.layout = Layout(
             Row(               
                Column('date_reception_courrier'),
                Column('civilite'),
                Column('nom'),
                ),
            Row(
                
                Column('fonction'),
                Column('matricule'),
                Column('date_embauche'),
                ),    
            Row(
                Column('categorie'),
                Column('numero_cnps'),  
                Column('duree_de_preavis'),        
                ),
            Row(    
                Column('duree_de_preavis_en_toute_lettre'),
                Column('indemnite_compensatrice'),
                ),   
            Row(
                Column('pret_scolaire'),
                Column('remboursement_PS'),
            ),     
                  
            Row(
                Column('nom_responsable', css_class="rows=10"),
                Column('fonction_responsable', css_class="rows=10"),
                Column('reference_lettre'),
                
               ),
            Submit('submit', 'Envoyer', css_class="btn btn-primary w-100 m-0")
        )

    def clean(self) : 
        rembourse = self.cleaned_data.get('remboursement_PS')
        pret_sco = self.cleaned_data.get('pret_scolaire')
        if  rembourse >= pret_sco : 
            raise forms.ValidationError('Le Montant restant après le remboursement du Prêt Scolaire doit être inférieur au Prêt Scolaire')
        #return super().clean()

        


  