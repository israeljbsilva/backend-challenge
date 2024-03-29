import json

from http import HTTPStatus


RESOURCE_PATH = '/api/v1'


def test_should_create_pet(customer_client, person, create_token):
    # GIVEN
    pet_data = {
        'name': 'Fred',
        'person': person.id
    }

    # WHEN
    response = customer_client.post(
        f'{RESOURCE_PATH}/pet', data=json.dumps(pet_data), content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # THEN
    assert response.status_code == HTTPStatus.CREATED

    content = json.loads(response.content.decode())
    assert content.get('id') == 1
    assert content.get('name') == 'Fred'
    assert content.get('resource_uri') == 'http://testserver/api/v1/pet/1'
    assert content.get('person') == person.id


def test_should_not_create_name_pet(customer_client, person, create_token):
    # GIVEN
    pet_data = {
        'person': person.id
    }

    # WHEN
    response = customer_client.post(
        f'{RESOURCE_PATH}/pet', data=json.dumps(pet_data), content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # THEN
    assert response.status_code == HTTPStatus.BAD_REQUEST

    content = json.loads(response.content.decode())
    assert content == {'name': ['This field is required.']}


def test_should_not_create_pet_with_invalid_person(customer_client, create_token):
    # GIVEN
    pet_data = {
        'name': 'Fred',
        'person': 0
    }

    # WHEN
    response = customer_client.post(
        f'{RESOURCE_PATH}/pet', data=json.dumps(pet_data), content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # THEN
    assert response.status_code == HTTPStatus.BAD_REQUEST

    content = json.loads(response.content.decode())
    assert content.get('person')[0] == 'Invalid pk "0" - object does not exist.'


def test_should_list_pet(customer_client, person, create_token):
    # GIVEN
    pet_data = {
        'name': 'Fred',
        'person': person.id
    }
    customer_client.post(f'{RESOURCE_PATH}/pet', data=json.dumps(pet_data), content_type='application/json',
                         HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # WHEN
    response = customer_client.get(f'{RESOURCE_PATH}/pet', content_type='application/json',
                                   HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # THEN
    assert response.status_code == HTTPStatus.OK

    content = json.loads(response.content.decode())
    assert content.get('results')[0] == {
        'id': 1,
        'name': 'Fred',
        'resource_uri': 'http://testserver/api/v1/pet/1',
        'person': {
            'id': 1,
            'name': 'Israel',
            'resource_uri':
                'http://testserver/api/v1/person/1'
        }
    }


def test_should_retrieve_pet(customer_client, person, create_token):
    # GIVEN
    pet_data = {
        'name': 'Fred',
        'person': person.id
    }
    customer_client.post(f'{RESOURCE_PATH}/pet', data=json.dumps(pet_data), content_type='application/json',
                         HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # WHEN
    response = customer_client.get(f'{RESOURCE_PATH}/pet/1', content_type='application/json',
                                   HTTP_AUTHORIZATION=f'Bearer {create_token}')

    # THEN
    assert response.status_code == HTTPStatus.OK

    content = json.loads(response.content.decode())
    assert content == {
        'id': 1,
        'name': 'Fred',
        'resource_uri': 'http://testserver/api/v1/pet/1',
        'person': {
            'id': 1,
            'name': 'Israel',
            'resource_uri':
                'http://testserver/api/v1/person/1'
        }
    }
