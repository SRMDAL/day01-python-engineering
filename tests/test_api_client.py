from app.api_client import get_headers, get_user, create_user
import pytest
import requests


def test_get_headers():
    result = get_headers("abc123")
    assert result == {"Authorization": "Bearer abc123"}




def test_get_user(monkeypatch):

    # Instead of actually contacting JSONPlaceholder, pretend that requests.get() returned our FakeResponse
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "id": 5,
                "name": "Chelsey Dietrich"
            }


    received_url = None
    def fake_get(url, headers, timeout):
        # The received_url I'm talking about belongs to the surrounding function. Don't create a new local one.
        nonlocal received_url
        received_url = url
        return FakeResponse()

    # Temporarily replace requests.get inside app.api_client with my fake_get function
    monkeypatch.setattr("app.api_client.requests.get", fake_get)


    result = get_user(5)

    assert received_url == "https://jsonplaceholder.typicode.com/users/5"
    assert result == {
            "id": 5,
            "name": "Chelsey Dietrich"
            }




def test_get_user_http_error(monkeypatch):

    class FakeResponse:
        def raise_for_status(self):
            raise requests.exceptions.HTTPError()

    def fake_get(url, headers, timeout):
        return FakeResponse()

    monkeypatch.setattr("app.api_client.requests.get", fake_get)

    with pytest.raises(requests.exceptions.HTTPError):
        get_user(5)




def test_create_user(monkeypatch):

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "name": "Chelsey",
                "email": "Chelsey@gmail.com"
            }


    received_url = None
    received_data = None
    def fake_post(url, headers, json, timeout):

        nonlocal received_url
        received_url = url

        nonlocal received_data
        received_data = json
        return FakeResponse()

    monkeypatch.setattr("app.api_client.requests.post", fake_post)

    result = create_user("Chelsey","Chelsey@gmail.com")

    assert received_url == 'https://jsonplaceholder.typicode.com/users'

    assert received_data == {
                "name": "Chelsey",
                "email": "Chelsey@gmail.com"
            }


    assert result == {
            "name": "Chelsey",
            "email": "Chelsey@gmail.com"
            }




def test_create_user_http_error(monkeypatch):

    class FakeResponse:
        def raise_for_status(self):
            raise requests.exceptions.HTTPError()

    def fake_post(url, headers, json, timeout):
        return FakeResponse()

    monkeypatch.setattr("app.api_client.requests.post", fake_post)

    with pytest.raises(requests.exceptions.HTTPError):
        create_user("Chelsey","Chelsey@gmail.com")
