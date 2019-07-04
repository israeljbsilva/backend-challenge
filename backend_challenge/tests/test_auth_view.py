import json

from http import HTTPStatus

from django.contrib.auth.models import User


RESOURCE_PATH = '/api/v1'


def test_should_create_auth(customer_client):
    # GIVEN
    User.objects.create_superuser(username="test", email='test@test.com', password="test")

    response = customer_client.post(f'{RESOURCE_PATH}/auth', data={'username': 'test', 'password': "test"})

    assert response.status_code == HTTPStatus.OK

    content = json.loads(response.content.decode())
    assert type(content) == dict
