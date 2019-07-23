from django.db import models
from attractions.models import Attractions
from comments.models import Comments
from assessments.models import Assessments
from adresses.models import Adresses

# Create your models here.


class TouristSpot(models.Model):
    name = models.CharField('Nome', max_length=150)
    descriptions = models.TextField('Descrição')
    approved = models.BooleanField('Aprovado', default=False)
    attractions = models.ManyToManyField(Attractions, verbose_name='Atrações')
    comments = models.ManyToManyField(Comments, verbose_name='Comentários')
    assessments = models.ManyToManyField(Assessments, verbose_name='Avaliações')
    adresses = models.ForeignKey(Adresses, verbose_name='Endereço', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turístico'
        ordering = ['name']

    def __str__(self):
        return self.name
