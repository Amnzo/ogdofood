from django.db import models

# Create your models here.


class Produit(models.Model):
    nom=models.CharField(max_length=40)
    prix_achat = models.FloatField()
    prix_vente_gros=models.FloatField()
    prix_vente_detaill=models.FloatField()
    def __str__(self):
        return f'{self.nom}'
    
    
    


