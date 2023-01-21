from django.contrib import admin

from Vendeur.models import Objectif, Vendeur

# Register your models here.

class VendeurAdmin(admin.ModelAdmin):
    list_display = [
        'nom',
        'salaire',
        'is_gros',
        'has_objectif',
        'Gasoil',
        'Chiffre',
        'Arba7',
     

    ]
    list_filter = ['nom','salaire']
    search_fields = ['nom', 'salaire']
    
    
    
  

admin.site.register(Vendeur,VendeurAdmin)

class ObjectifAdmin(admin.ModelAdmin):
    list_display = [
        'total_object',
        'prime_objectif',


    ]
    list_filter = ['total_object',
        'prime_objectif',]
    search_fields = ['total_object',
        'prime_objectif',]

admin.site.register(Objectif,ObjectifAdmin)
