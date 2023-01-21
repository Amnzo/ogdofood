from django import forms
from django.forms.fields import DateField
from django.forms.widgets import NumberInput
from django.conf import settings
# creating a form
class StatiqueForm(forms.Form):

        du=forms.DateField(required =True,widget=forms.widgets.DateInput(attrs= {'type': 'date'}), input_formats=settings.DATE_INPUT_FORMATS)
        au=forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), input_formats=settings.DATE_INPUT_FORMATS)
        def clean(self):
                cleaned_data = super().clean()
                start_date = cleaned_data.get("du")
                end_date = cleaned_data.get("au")
                print("Cleaaaned data")
                if end_date < start_date:
                        print(f'clenned one {start_date}')
                        print(f'clenned otwone {end_date}')
                        raise forms.ValidationError("La date Fin  doit etre superieur a la date de début   .")
