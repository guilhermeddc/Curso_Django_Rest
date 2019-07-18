from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Assessments(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    comment = models.TextField('Comentário', null=True, blank=True)
    note = models.DecimalField('Nota', decimal_places=2, max_digits=3)
    date = models.DateTimeField('Data', auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['user']

    def __str__(self):
        return self.user.username

