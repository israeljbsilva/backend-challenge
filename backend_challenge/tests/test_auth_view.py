import json

from http import HTTPStatus

from django.contrib.auth.models import User


RESOURCE_PATH = '/api/v1'


def test_should_create_auth(customer_client):
    # GIVEN
    User.objects.create_superuser(username="test", email='test@test.com', password="test")

    # WHEN
    response = customer_client.post(f'{RESOURCE_PATH}/auth', data={'username': 'test', 'password': "test"})

    # THEN
    assert response.status_code == HTTPStatus.OK

    content = json.loads(response.content.decode())
    assert type(content) == dict


def test_should_not_create_auth_without_super_user(customer_client):
    # GIVEN

    # WHEN
    response = customer_client.post(f'{RESOURCE_PATH}/auth', data={'username': 'test', 'password': "test"})

    # THEN
    assert response.status_code == HTTPStatus.UNAUTHORIZED

    content = json.loads(response.content.decode())
    assert content.get('detail') == 'No active account found with the given credentials'


def test_should_not_create_auth_with_invalid_credentials(customer_client):
    # GIVEN
    User.objects.create_superuser(username="test", email='test@test.com', password="test")

    # WHEN
    response = customer_client.post(f'{RESOURCE_PATH}/auth', data={})

    # THEN
    assert response.status_code == HTTPStatus.BAD_REQUEST

    content = json.loads(response.content.decode())
    assert content == {'username': ['This field is required.'], 'password': ['This field is required.']}
