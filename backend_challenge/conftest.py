import pytest
import json

from pytest_factoryboy import register

from .factories import PersonFactory, PetFactory, UserFactory


register(PersonFactory)
register(PetFactory)
register(UserFactory)


@pytest.fixture
def customer_client(db):
    from django.test.client import Client
    return Client()


@pytest.fixture
def create_token(customer_client):
    user = UserFactory.create()
    response_auth = customer_client.post('/api/v1/auth', data={'username': user.username, 'password': '123456'})
    content_auth = json.loads(response_auth.content.decode())
    return content_auth["access"]
