import pytest

from pytest_factoryboy import register

from .factories import PersonFactory, PetFactory


register(PersonFactory)
register(PetFactory)


@pytest.fixture
def customer_client(db):
    from django.test.client import Client
    return Client()
