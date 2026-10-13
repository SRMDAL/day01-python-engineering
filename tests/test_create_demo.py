from app import api_client
from app.create_demo import main
import requests


def test_main_empty_input(monkeypatch, capsys):
    def fake_create_user(name, email):
        raise AssertionError("API should not be called")

    monkeypatch.setattr(api_client, "create_user", fake_create_user)
    monkeypatch.setattr("builtins.input", lambda prompt: "")

    main()

    captured = capsys.readouterr()
    assert captured.out == "Name and email cannot be empty.\n"




def test_main_success(monkeypatch, capsys):
    def fake_input(prompt):
        if prompt == "Enter your name: ":
            return "Saghar"
        if prompt == "Enter your email: ":
            return "saghar@example.com"

    def fake_create_user(name, email):
        return {
            "id": 11,
            "name": name,
            "email": email
        }

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr(api_client, "create_user", fake_create_user)

    main()

    captured = capsys.readouterr()

    assert captured.out == (
        "User created successfully:\n"
        "{'id': 11, 'name': 'Saghar', 'email': 'saghar@example.com'}\n"
    )



def test_main_success_logs_info(monkeypatch, caplog):
    caplog.set_level("INFO")

    def fake_input(prompt):
        if prompt == "Enter your name: ":
            return "Saghar"
        if prompt == "Enter your email: ":
            return "saghar@example.com"

    def fake_create_user(name, email):
        return {
            "id": 11,
            "name": name,
            "email": email
        }

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr(api_client, "create_user", fake_create_user)

    main()

    assert "User creation request succeeded." in caplog.text
    assert caplog.records[1].levelname == "INFO"



def test_main_http_error(monkeypatch, capsys):
    def fake_input(prompt):
        if prompt == "Enter your name: ":
            return "Saghar"
        if prompt == "Enter your email: ":
            return "saghar@example.com"

    def fake_create_user(name, email):
        raise requests.exceptions.HTTPError()

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr(api_client, "create_user", fake_create_user)

    main()

    captured = capsys.readouterr()
    assert captured.out == (
        "The server rejected the request. Please try again.\n"
    )






def test_main_timeout(monkeypatch, capsys):
    def fake_input(prompt):
        if prompt == "Enter your name: ":
            return "Saghar"
        if prompt == "Enter your email: ":
            return "saghar@example.com"

    def fake_create_user(name, email):
        raise requests.exceptions.Timeout()

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr(api_client, "create_user", fake_create_user)

    main()

    captured = capsys.readouterr()
    assert captured.out == "Request timed out. Please try again later.\n"




def test_main_connection_error(monkeypatch, capsys):
    def fake_input(prompt):
        if prompt == "Enter your name: ":
            return "Saghar"
        if prompt == "Enter your email: ":
            return "saghar@example.com"

    def fake_create_user(name, email):
        raise requests.exceptions.ConnectionError()

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr(api_client, "create_user", fake_create_user)

    main()

    captured = capsys.readouterr()
    assert captured.out == (
        "Connection error. Please check your internet connection.\n"
    )




def test_main_empty_input_logs_warning(monkeypatch, caplog):
    monkeypatch.setattr("builtins.input", lambda prompt: "")

    caplog.set_level("WARNING")
    main()

    assert "User creation cancelled because name or email was empty." in caplog.text
    assert caplog.records[0].levelname == "WARNING"



