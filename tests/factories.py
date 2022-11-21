from datetime import date

import factory

from ads.models import Ad, Category
from selection.models import Selection
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = 'unq'
    slug = factory.Faker('ean', length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker(provider='name')
    password = 'test_password'
    birth_date = date(1982, 12, 30)
    first_name = 'test_first_name'


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = 'test_names'
    price = 12
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
