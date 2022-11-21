import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad):
    expected_response = {
        "id": ad.pk,
        "author_id": ad.author_id,
        "author": ad.author.first_name,
        "category_id": ad.category_id,  #
        "name": 'test_names',
        "price": 12,
        "description": None,
        "is_published": False,
    }
    response = client.get(f'/ads/{ad.pk}/')

    assert response.status_code == 200, 'ads_retrieve статус-код не совпал'
    assert response.data == expected_response, 'ads_retrieve data не совпала'
