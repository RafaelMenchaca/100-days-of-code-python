import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "your_api_key_here"
account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"

weather_params = {
    "lat": 37.215519,
    "lon": -93.292358,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# for hour_data in weather_data
will_rain = False
for hour_data in weather_data["weather"]:
    condition_code = hour_data["id"]
    # print(condition_code)
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    #  FOR SMS IT IS NOT AVAILABLE IN THE FREE VERSION
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an umbrella",
    #     from_="+twilio_number_here",
    #     to="+your_number_here",
    # )
    
    # Whats App
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella",
    from_='whatsapp:+twilio_number_here',
    to='whatsapp:+your_number_here',
    )
    
    print(message.status)
else:
    print("No umbrella needed")
    