import pytest

from backend_challenge.serializers import PersonSerializer


pytestmark = [pytest.mark.django_db, pytest.mark.serial]


def test_should_serialize_person(person):
    # GIVEN
    # WHEN
    serializer = PersonSerializer(person)

    # THEN
    assert isinstance(serializer.context, dict)
    assert serializer.instance.id == 1
    assert serializer.instance.name == 'Israel'


def test_should_deserialize_person():
    # GIVEN
    person_id = 1
    person_data = {
        'id': person_id,
        'name': 'Israel'
    }

    # WHEN
    serializer = PersonSerializer(data=person_data)

    # THEN
    assert serializer.is_valid()

    person = serializer.save(id=person_id)
    assert person.id
    assert person.name == 'Israel'
