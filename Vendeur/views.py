import datetime
from django.shortcuts import render
from urllib3 import HTTPResponse
from django.db.models import Sum
# Create your views here.
from django.http import HttpResponse

from Charge.models import Charge, ProduitCharger
from Depense.models import Depense_dynamique, Depense_statique
from Gasoil.models import Gasoil
from Vendeur.forms import StatiqueForm
from Vendeur.models import Vendeur
from django.utils.dateparse import parse_date
from django.utils.dateparse import parse_datetime
def index(request):
    chiffre_charges_mois=0
    benifice_charges_mois=0
    essence_charges_mois=0
    dynamique_mois=0
    days=0
    
    if request.method =='POST' :
        form = StatiqueForm(request.POST)
        if form.is_valid():
            print("------validate Post-----------")
            date_from = parse_datetime(request.POST['du'])
            date_au = parse_datetime(request.POST['au'])
            print(type(date_from))
            print(date_from.month)
            print(date_from.day)
            print(date_from.year)


            for one_chage in Charge.objects.filter(date__range=(date_from, date_au)):
                chiffre_charges_mois=chiffre_charges_mois+one_chage.Vente()
                benifice_charges_mois=benifice_charges_mois+one_chage.Benifice()
                
            for one_essence in Gasoil.objects.filter(date__range=(date_from, date_au)):
                essence_charges_mois=essence_charges_mois+one_essence.montant
                print( essence_charges_mois)
                #benifice_charges_mois=benifice_charges_mois+one_chage.Benifice()
            for one_dynamique in Depense_dynamique.objects.filter(date__range=(date_from, date_au)):
                dynamique_mois=dynamique_mois+one_dynamique.montant
                
                #benifice_charges_mois=benifice_charges_mois+one_chage.Benifice()
            delta =date_au - date_from
            days=delta.days
                
                

            
        form = StatiqueForm(initial={'du': request.POST.get('du', ''), 'au': request.POST.get('au', '')})
    else:
        form = StatiqueForm()
        
            
        #print(request.POST['du'])
    charges=Charge.objects.all()
    vente_general=0
    benifice_mois=0
    today = datetime.datetime.now()
    for charge in  charges:
        vente_general=vente_general+charge.Vente()
    month_wins=Charge.objects.filter(date__year=today.year, date__month=today.month)
    for win in month_wins:
        benifice_mois=benifice_mois+charge.Benifice()
    #top_produit=ProduitCharger.objects.values("produit__nom").annotate(sum=Sum('quantity')).order_by("quantity").last()
   
    
    benifice=0
    statique=0
    dynamique=0
    for chargestatique in  Depense_statique.objects.all():
        statique=statique+chargestatique.montant
        print(statique)
    for chargesdynamqie in Depense_dynamique.objects.filter(date__year=today.year, date__month=today.month):
        dynamique=dynamique+chargesdynamqie.montant
    saliares=0
    for vendeur in  Vendeur.objects.all():
        saliares=saliares+vendeur.salaire
    
    benifice=0
    #charges_benifice=
    for charge in  month_wins:
        benifice=benifice+charge.Benifice()
  
    gasoil=0
    for essence in  Gasoil.objects.filter(date__year=today.year, date__month=today.month):
        gasoil=gasoil+essence.montant
    
    total_c=statique+dynamique+saliares+gasoil
    benifice_total=benifice-total_c
    print(benifice_total)
        
    
    context={"benifice_charges_mois":benifice_charges_mois,
             "chiffre_charges_mois":chiffre_charges_mois,
             "essence_charges_mois":essence_charges_mois,
              "statique_mois":statique,
              "dynamique_mois":dynamique_mois,
              "days":days,
             
             
        
        'totalcharges': vente_general,'total_month':benifice_mois,
             'chargesttq':total_c,'form':form}
    return render(request,'ecom/admin_dashboard.html',context)
