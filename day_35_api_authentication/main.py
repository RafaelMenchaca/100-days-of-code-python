import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "f056e46a3cdff5f4f52899466446a32c"

weather_params = {
    "lat": 43.051868,
    "lon": -91.389893,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())