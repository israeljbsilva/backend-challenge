import pytest

from backend_challenge.models import Person, Pet


pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_should_create_person(person):
    assert Person.objects.count() == 1
    assert person.name == 'Israel'


def test_should_create_pet(pet, person):
    assert Pet.objects.count() == 1
    assert pet.name == 'Fred'
    assert pet.person.id == person.id
