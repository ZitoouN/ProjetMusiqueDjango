from django.db import models

# Create your models here.

class Musique(models.Model):
    titre = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    date_parution = models.DateField(blank = True, null = True)
    min = models.IntegerField(blank=False)
    sec = models.IntegerField(blank=False)
    commentaire = models.TextField(null = True, blank = True)

    def __str__(self):
        string = f"Le son {self.titre} est composé par {self.artiste} le {self.date_parution} qui a une durée de {self.min}:{self.sec} min"
        return string

    def dico(self):
        return {"titre":self.titre, "artiste":self.artiste, "date_parution":self.date_parution, "min":self.min, "sec":self.sec, "commentaire":self.commentaire}

class Album(models.Model):
    nom = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    date = models.DateField(blank = True, null = True)

    def __str__(self):
        string = f"Album nommé {self.nom} est crée par {self.artiste} le {self.date}"
        return string

    def dico2(self):
        return {"nom":self.nom, "artiste":self.artiste, "date":self.date}