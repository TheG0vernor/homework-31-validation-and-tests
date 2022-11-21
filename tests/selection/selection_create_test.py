import pytest


@pytest.mark.django_db
def test_create_select(client, ad, moderator_token):
    expected_response = ...
