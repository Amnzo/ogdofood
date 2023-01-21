from django.db import models

from Produit.models import Produit
from Vendeur.models import Vendeur

# Create your models here.

class Charge(models.Model):
    vendeur=models.ForeignKey(Vendeur,related_name='charges', on_delete=models.CASCADE,null=False)
    date= models.DateField(blank=True,null=False)
    class Meta:
        constraints = [ models.UniqueConstraint(fields=('vendeur', 'date'), name='once_per_vendeur') ]
        
    def __str__(self):
        return f' {self.vendeur.nom}  -----{self.date}'
    
    
    def get_products(self):
        return "\n".join([f'{p.quantity}:{p.produit.nom}' for p in self.produits.all()])
    
    def Vente(self):
        charges=self.produits.all()
        montant=0
        for ligne in charges:
            #print(ligne.produit.prix_achat*ligne.quantity)
            if self.vendeur.is_gros:
                montant=montant+(ligne.produit.prix_vente_gros*ligne.quantity)
            else:
                montant=montant+(ligne.produit.prix_vente_detaill*ligne.quantity)
        #print(montant)
        return montant
    
    
    def Benifice(self):
        charges=self.produits.all()
        montant=0
        benifice=0
        for ligne in charges:

            if self.vendeur.is_gros:
                achat=ligne.produit.prix_achat*ligne.quantity
                vente=ligne.produit.prix_vente_gros*ligne.quantity
                benifice=benifice+(vente-achat)

            else:
                achat=ligne.produit.prix_achat*ligne.quantity
                vente=ligne.produit.prix_vente_detaill*ligne.quantity
                benifice=benifice+(vente-achat)


            #print(benifice)
        #print("-------------------------------")
        return benifice
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




class ProduitCharger(models.Model):
    charge=models.ForeignKey(Charge,related_name='produits', on_delete=models.CASCADE,null=False)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False,null=False)


    class Meta:
        constraints = [  models.UniqueConstraint(fields=('produit', 'charge'), name='once_per_product_sale')]
    def __str__(self):
        return f' {self.quantity}: {self.produit.nom} ' 
    
    
    
    
    


    

    
    #maroc@6271 code wifi
  

