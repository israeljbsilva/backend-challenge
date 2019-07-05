import pytest

from backend_challenge.serializers import PetSerializer


pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_should_serialize_pet(person, pet):
    # GIVEN
    # WHEN
    serializer = PetSerializer(pet)

    # THEN
    assert isinstance(serializer.context, dict)
    assert serializer.instance.id == 1
    assert serializer.instance.name == 'Fred'
    assert serializer.instance.person.id == person.id


def test_should_deserialize_pet(person):
    # GIVEN
    pet_id = 1
    pet_data = {
        'id': pet_id,
        'name': 'Fred',
        'person': person.id
    }

    # WHEN
    serializer = PetSerializer(data=pet_data)

    # THEN
    assert serializer.is_valid()

    pet = serializer.save(id=pet_id)
    assert pet.id
    assert pet.name == 'Fred'
    assert pet.person.id == person.id
