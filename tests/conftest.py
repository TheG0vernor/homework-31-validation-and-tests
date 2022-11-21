from pytest_factoryboy import register

from tests.factories import AdFactory, UserFactory, CategoryFactory, SelectionFactory

pytest_plugins = 'tests.fixtures'

register(AdFactory)
register(CategoryFactory)
register(UserFactory)
register(SelectionFactory)
