from django.db import models
from attractions.models import Attractions
from comments.models import Comments
from assessments.models import Assessments
from adresses.models import End


# Create your models here.


class TouristSpot(models.Model):
    name = models.CharField('Nome', max_length=150)
    descriptions = models.TextField('Descrição')
    approved = models.BooleanField('Aprovado', default=False)
    attractions = models.ManyToManyField(Attractions, verbose_name='Atrações')
    comments = models.ManyToManyField(Comments, verbose_name='Comentários')
    assessments = models.ManyToManyField(Assessments, verbose_name='Avaliações')
    end = models.ForeignKey(End, verbose_name='Endereço', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='tourist-spot', null=True, blank=True)

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turístico'
        ordering = ['name']

    @property
    def description_complete_two(self):
        return '%s - %s' % (self.name, self.descriptions)

    def __str__(self):
        return self.name
