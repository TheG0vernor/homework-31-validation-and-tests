from django.core import validators
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=10, validators=[validators.MinLengthValidator(limit_value=5)], unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=60, validators=[validators.MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    price = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
