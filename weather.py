import requests

def get_weather(city, api_key):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Cannot retrieve weather data...")
    data = response.json()
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["main"]
    }