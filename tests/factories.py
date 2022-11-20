import factory

from ads.models import Ad, Category
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = 'unq'
    slug = '1621w'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker(provider='name')
    password = 'test_password'


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = 'test_name'
    price = 12
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
