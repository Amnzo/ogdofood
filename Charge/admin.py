from django.contrib import admin

from Charge.models import Charge, ProduitCharger

# Register your models here.
class ChargeAdmin(admin.ModelAdmin):
    list_display = [
        'vendeur',
        'date',
        'get_products',
        'Vente',
        'Benifice'

    ]
    


        
    
    list_filter = ['vendeur','date'
 ]
    search_fields = ['vendeur','date']

admin.site.register(Charge,ChargeAdmin)



class ProduitChargerAdmin(admin.ModelAdmin):
    list_display = [
        'produit',
        'quantity',
        'charge'


    ]
    
    list_filter = ['charge','produit']
    search_fields = ['charge','produit']

admin.site.register(ProduitCharger,ProduitChargerAdmin)