from django.contrib import admin

from Produit.models import Produit

# Register your models here.
class ProduitAdmin(admin.ModelAdmin):
    list_display = [
        'nom',
        'prix_achat',
        'prix_vente_gros',
        'prix_vente_detaill',

    ]
    
    list_filter = ['nom',
 ]
    search_fields = ['nom']

admin.site.register(Produit,ProduitAdmin)