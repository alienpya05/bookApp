from django.db import models

# Create your models here.


class Livre(models.Model):
    titre = models.CharField(max_length=10)
    auteur = models.CharField(max_length=10)
    datePublication = models.DateField()
    image = models.ImageField(upload_to='image_livre/')
    note =  models.IntegerField()
    commentaire = models.TextField()