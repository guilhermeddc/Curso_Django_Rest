# Generated by Django 2.2.4 on 2019-09-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=150, verbose_name='Linha 1')),
                ('line2', models.CharField(blank=True, max_length=150, null=True, verbose_name='Linha 2')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['line1', 'line2'],
            },
        ),
    ]
