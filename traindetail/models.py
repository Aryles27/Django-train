from django.db import models

# Create your models here.

"""
Train 
- nom 
- ligne
- type (long / court)
- heure depart
- heure d'arrivée
- destination
- detail trajet => image
"""

class Train(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128)
    ligne = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    heure_depart = models.TimeField()
    heure_arrivee = models.TimeField()
    duree_trajet = models.DurationField()
    destination = models.CharField(max_length=100)
    detail_trajet = models.ImageField(upload_to="detail", blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.ligne}) ({self.destination})"


