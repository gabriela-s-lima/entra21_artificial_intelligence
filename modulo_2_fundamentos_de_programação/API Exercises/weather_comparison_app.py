import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from .env file
api_key = os.getenv("API_KEY_WEATHER")


def get_weather_data(city, api_key):
    """
    Fetches weather data for a given city from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return {
            'city': city,
            'error': f"Could not retrieve data for '{city}' (Status {response.status_code})"
        }


def display_results(cities_info):
    """
    Displays the weather results and identifies the hottest city.
    """
    print("\n=== Results ===")
    for info in cities_info:
        if 'error' in info:
            print(f"[{info['city']}] -> Error: {info['error']}")
        else:
            print(f"[{info['city']}] -> {info['temperature']}°C, {info['description'].capitalize()}")

    valid_cities = [c for c in cities_info if 'error' not in c]
    if valid_cities:
        hottest = max(valid_cities, key=lambda x: x['temperature'])
        print(f"\n🔥 The hottest city is {hottest['city']} with {hottest['temperature']}°C.")
    else:
        print("\nNo valid cities to compare temperatures.")


def main():
    """
    Main function that asks for city input, fetches data, and shows results.
    """
    api_key = os.getenv("API_KEY_WEATHER")
    cities = input("Enter at least 3 cities separated by commas: ").split(',')

    if len(cities) < 3:
        print("You must provide at least 3 cities.")
        return

    cities = [city.strip() for city in cities]
    data = [get_weather_data(city, api_key) for city in cities]
    display_results(data)


if __name__ == "__main__":
    main()
