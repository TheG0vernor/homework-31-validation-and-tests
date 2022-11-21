from datetime import date

import pytest


@pytest.fixture
@pytest.mark.django_db
def moderator_token(client, django_user_model):
    username = 'val'
    password = '6'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role='moderator',
        birth_date=date(1982, 12, 30)

    )
    response = client.post(
        path='/users/login/',
        data={'username': username, 'password': password},
        content_type='application/json'
    )
    return response.data['token']
