from django.db import models

from ads.models import Ad
from users.models import User


class Selection(models.Model):
    name = models.CharField(max_length=40)
    items = models.ManyToManyField(to=Ad)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name_plural = 'Подборки'
        verbose_name = 'Подборка'

    def __str__(self):
        return self.name
