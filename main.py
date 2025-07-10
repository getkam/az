from config import API_KEY
from weather import get_weather

def main():
    city = "Warsaw"
    try:
        weather = get_weather(city, API_KEY)
        print(f"Weather in {weather['city']}: {weather['temp']}°C, {weather['desc']}")
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()
