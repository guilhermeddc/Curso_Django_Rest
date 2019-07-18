from django.db import models

# Create your models here.


class Adresses(models.Model):
    line1 = models.CharField('Linha 1', max_length=150)
    line2 = models.CharField('Linha 2', max_length=150, null=True, blank=True)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100)
    country = models.CharField('País', max_length=100)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['line1', 'line2']

    def __str__(self):
        return self.line1
