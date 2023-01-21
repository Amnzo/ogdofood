from django.contrib import admin

from Gasoil.models import Gasoil

# Register your models here.
class Gasoildmin(admin.ModelAdmin):
    list_display = [
        'vendeur',
        'montant',
        'date',
        

    ]
    list_filter = [ 'vendeur','date']
    search_fields = ['vendeur', 'date']

admin.site.register(Gasoil,Gasoildmin)