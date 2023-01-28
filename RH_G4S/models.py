from django.db import models

# Create your models here.

# class Personne(models.Model):

#    liste_1 = (("Monsieur", "Monsieur"), ("Madame","Madame"), ("Mademoiselle", "Mademoiselle"))
#    liste_2 = (("1ere", "1ere"), ("2e","2e" ), ("3e","3e" ), ("4e","4e" ), ("5e","5e" ), ("6e","6e" ), 
            #    ("7e","7e" ), ("8e","8e" ), ("9e","9e" ), ("10e","10e" ))
""""
    civilite = models.CharField(choices = liste_1, default="Monsieur")
    nom= models.CharField(max_length=40)
    prenom= models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    matricule = models.IntegerField()
    date_embauche = models.DateField()
    categorie = models.CharField(choices = liste_2, default="1ere")
    numero_cnps = models.IntegerField()
    duree_de_preavis = models.CharField(max_length=40)
    duree_de_preavis_en_toute_lettre = models.CharField(max_length=100)
    indemnite_compensatrice = models.IntegerField()
    pret_scolaire = models.IntegerField()
    responsable_en_lettre = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)

"""    