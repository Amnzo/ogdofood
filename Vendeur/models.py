from django.db import models

# Create your models here.
class Objectif(models.Model):

    total_object=models.FloatField()
    prime_objectif=models.FloatField()
    
    def __str__(self):
        return f'si total vente = {self.total_object} tu gagne : {self.prime_objectif}'


class Vendeur(models.Model):
    nom=models.CharField(max_length=40)
    is_gros=models.BooleanField(default=False)
    salaire=models.FloatField()
    has_objectif=models.ForeignKey(
        'Objectif', related_name='vendeurs', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nom} '
    
    
    def Chiffre(self):
        charges=self.charges.all()
        chiffre=0
        for ligne in charges:
            
            chiffre=chiffre+ligne.Vente()
        return chiffre
    
    
    def Arba7(self):
        charges=self.charges.all()
        gant=0
        for ligne in charges:
            
            gant=gant+ligne.Benifice()
        return gant
    
    
    def Gasoil(self):
        gasoils=self.gasoils.all()
        total=0
        for ligne in gasoils:
            total=total+ligne.montant            

        return total
            

    
    
    
