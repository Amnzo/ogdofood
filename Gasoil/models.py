from django.db import models

from Vendeur.models import Vendeur

# Create your models here.
class Gasoil(models.Model):
    vendeur = models.ForeignKey(Vendeur,related_name='gasoils',  on_delete=models.CASCADE)
    montant = models.FloatField(null=False,blank=False)
    date = models.DateField(null=False,blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('vendeur', 'date'), name='once_per_vendeur_date')
        ]
    def __str__(self):
        return f' {self.vendeur.nom}-{self.montant}-{self.date}'
    
    
    
