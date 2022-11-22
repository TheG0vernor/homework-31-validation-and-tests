import pytest


@pytest.mark.django_db
def test_create_select(client, ad, user, moderator_token):
    expected_response = {
        "id": 1,
        "name": "test_name",
        "items": [ad.pk],
        "owner": user.id
    }
    data = {
        "name": "test_name",
        "items": [ad.pk],
    }
    response = client.post(
            path='/selection/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + moderator_token,
            data=data
        )

    assert response.status_code == 201
    assert response.data == expected_response
