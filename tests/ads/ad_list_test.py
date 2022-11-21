import pytest

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ads = AdFactory.create_batch(9)  # кол-во записей в списке для тестирования
    expected_response = {
        'count': 9,
        'next': None,
        'previous': None,
        'results': AdListSerializer(instance=ads, many=True).data
    }

    response = client.get('/ads/')

    assert response.status_code == 200, 'ads статус не 200'
    assert response.data == expected_response, 'ads data не совпала'
