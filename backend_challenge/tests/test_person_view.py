import json

from http import HTTPStatus


RESOURCE_PATH = '/api/v1'


def test_should_create_person(customer_client):
    # GIVEN
    person_data = {
        'name': 'Israel'
    }

    # WHEN
    response = customer_client.post(
        f'{RESOURCE_PATH}/person', data=json.dumps(person_data), content_type='application/json')

    # THEN
    assert response.status_code == HTTPStatus.CREATED

    content = json.loads(response.content.decode())
    assert content.get('id') == 1
    assert content.get('name') == 'Israel'
    assert content.get('resource_uri') == 'http://testserver/api/v1/person/1'


def test_should_not_create_name_person(customer_client):
    # GIVEN
    person_data = {}

    # WHEN
    response = customer_client.post(
        f'{RESOURCE_PATH}/person', data=json.dumps(person_data), content_type='application/json')

    # THEN
    assert response.status_code == HTTPStatus.BAD_REQUEST

    content = json.loads(response.content.decode())
    assert content == {'name': ['This field is required.']}
