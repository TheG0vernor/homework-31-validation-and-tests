import pytest


@pytest.mark.django_db
def test_create_ad(client, ad, moderator_token):
    expected_response = {
        "id": 2,  # при несовпадении вернуть ad.pk
        "author": ad.author_id,
        "category": ad.category_id,
        "name": 'test_names',
        "price": 12,
        "description": None,
        "is_published": False,
        "image": None,
    }
    data = {
        "name": 'test_names',
        "price": 12,
        "category": ad.category_id,
        "author": ad.author_id
    }
    response = client.post(
        path='/ads/create/',
        HTTP_AUTHORIZATION='Token ' + moderator_token,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response
