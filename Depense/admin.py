from django.contrib import admin

from Depense.models import Depense_dynamique, Depense_statique

# Register your models here.
class Depense_S_Admin(admin.ModelAdmin):
    list_display = [
        'libelle',
        'montant',
        'date',


    ]
    
    list_filter = ['libelle','date'
 ]
    search_fields = ['libelle','date']

admin.site.register(Depense_statique,Depense_S_Admin)



class Depense_D_Admin(admin.ModelAdmin):
    list_display = [
        'libelle',
        'montant',
        'date',


    ]
    
    list_filter = ['libelle','date'
 ]
    search_fields = ['libelle','date']

admin.site.register(Depense_dynamique,Depense_D_Admin)
