# Generated by Django 4.1.4 on 2023-01-21 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depense', '0002_alter_depense_dynamique_montant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depense_dynamique',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]