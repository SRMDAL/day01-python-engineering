from app.api_client import get_headers


def test_get_headers():
    result = get_headers("abc123")
    assert result == {"Authorization": "Bearer abc123"}
