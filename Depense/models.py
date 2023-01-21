import datetime
from django.db import models

# Create your models here.
class Depense_statique(models.Model):
    libelle=models.CharField(max_length=40)
    montant = models.FloatField(null=False,blank=False)
    date= models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f' {self.libelle} {self.montant}'
    
class Depense_dynamique(models.Model):
    libelle=models.CharField(max_length=40)
    montant = models.FloatField(null=False,blank=False)
    date= models.DateField(blank=False,null=False,default=datetime.date.today)

    def __str__(self):
        return f' {self.libelle}  {self.montant}'
    
    
    
