# Generated by Django 2.2.1 on 2019-07-18 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_spot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='adresses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adresses.Adresses', verbose_name='Endereço'),
        ),
    ]
