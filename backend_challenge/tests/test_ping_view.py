from rest_framework.status import HTTP_200_OK


def test_should_get_ping(client):
    # GIVEN

    # WHEN
    response = client.get('/ping/')

    # THEN
    assert response.status_code == HTTP_200_OK
