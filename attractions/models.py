from django.db import models

# Create your models here.


class Attractions(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição')
    workingHours = models.TextField('Horário de Funcionamento')
    minimumAge = models.PositiveIntegerField('Idade Mínima')
    photo = models.ImageField(upload_to='attractions', null=True, blank=True)

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
        ordering = ['name']

    def __str__(self):
        return self.name

