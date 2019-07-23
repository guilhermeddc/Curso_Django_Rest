from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comments(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    comments = models.TextField('Comentários')
    date = models.DateTimeField('Data', auto_now_add=True)
    approved = models.BooleanField('Aprovado', default=False)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['user']

    def __str__(self):
        return self.user.username
