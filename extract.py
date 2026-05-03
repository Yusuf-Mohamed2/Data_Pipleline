import requests

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 30.0444,
        "longitude": 31.2357,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")

    return response.json()
print("Sucess!")