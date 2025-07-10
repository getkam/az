import pytest
from weather import get_weather

def test_get_weather_success(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                "name":"Brazil",
                "main":{"temp":33.87},
                "weather": [{"id": 804, "main": "Clouds"}]
            }

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    result = get_weather("Brazil", "whatever")
    assert result["city"] == "Brazil"
    assert result["temp"] == 33.87
    assert result["desc"] == "Clouds"