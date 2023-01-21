# Generated by Django 4.1.4 on 2023-01-18 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objectif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_object', models.FloatField()),
                ('prime_objectif', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('is_gros', models.BooleanField(default=False)),
                ('salaire', models.FloatField()),
                ('has_objectif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendeurs', to='Vendeur.objectif')),
            ],
        ),
    ]