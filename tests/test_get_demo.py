import requests
from app import api_client
from app.get_demo import main


def test_main_http_error(monkeypatch, capsys):

    def fake_get_user(user_id):
        raise requests.exceptions.HTTPError()

    monkeypatch.setattr("app.api_client.get_user", fake_get_user)

    monkeypatch.setattr("builtins.input", lambda prompt: "5")

    main()
    captured = capsys.readouterr()
    assert captured.out == "User could not be found. Please check the user ID and try again.\n"


def test_main_timeout(monkeypatch, capsys):

    def fake_get_user(user_id):
        raise requests.exceptions.Timeout()

    monkeypatch.setattr("app.api_client.get_user", fake_get_user)
    monkeypatch.setattr("builtins.input", lambda prompt: "5")

    main()

    captured = capsys.readouterr()
    assert captured.out == "Request timed out. Please try again later.\n"




def test_main_connection_error(monkeypatch, capsys):

    def fake_get_user(user_id):
        raise requests.exceptions.ConnectionError()


    monkeypatch.setattr("app.api_client.get_user", fake_get_user)
    monkeypatch.setattr("builtins.input", lambda prompt: "5")

    main()

    captured = capsys.readouterr()
    assert captured.out == "Connection error occurred. Please check your internet connection and try again.\n"



def test_main_success(monkeypatch, capsys):

    def fake_get_user(user_id):
        return {
            "id": 5,
            "name": "Chelsey Dietrich"
        }

    monkeypatch.setattr("app.api_client.get_user", fake_get_user)
    monkeypatch.setattr("builtins.input", lambda prompt: "5")

    main()
    captured = capsys.readouterr()
    assert captured.out == "{'id': 5, 'name': 'Chelsey Dietrich'}\n"