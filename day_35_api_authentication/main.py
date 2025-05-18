import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "f056e46a3cdff5f4f52899466446a32c"

weather_params = {
    "lat": 43.051868,
    "lon": -91.389893,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

# for hour_data in weather_data