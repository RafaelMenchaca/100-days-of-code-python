import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "yourmail@gmail.com"
MY_PASSWORD = "yourpassword"
MY_LAT = 41.878113
MY_LONG = -87.629799

def is_ss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Chicago"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    # Check if the ISS is overhead and it's night
    if is_ss_overhead() and is_night():
        conecction = smtplib.SMTP("smtp.gmail.com")
        conecction.starttls()
        conecction.login(MY_EMAIL, MY_PASSWORD) 
        conecction.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="recipientmail@gmail.com",
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )



# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
#     "tzid": "America/Chicago"
# }

# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()

# sunrise = data["results"]["sunrise"].split("T")[1]
# print(f"Sunrise: {sunrise}")
# sunset = data["results"]["sunset"].split("T")[1]
# print(f"Sunset: {sunset}")