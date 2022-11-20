from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)  # latitude (широта)
    lng = models.FloatField(blank=True, null=True)  # longitude (долгота)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    ROLE = [('member', 'участник'),
            ('moderator', 'модератор'),
            ('admin', 'администратор')]
    role = models.CharField(max_length=9, choices=ROLE, default='member')
    age = models.PositiveIntegerField(null=True, blank=True)
    locations = models.ManyToManyField(to=Location)
    birth_date = models.DateField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        # self.set_password(self.password)  # строчка дополнительного хеширования пароля для создания и редактирования пользователя в админке. любого, кроме созданного в консоли командой createsuperuser
        super().save(*args, **kwargs)
