import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")

NUTRIONIX_APP_ID = os.getenv("NUTRIONIX_APP_ID")
NUTRIONIX_API_KEY = os.getenv("NUTRIONIX_API_KEY")
GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 185
AGE = 27

nutrionix_headers = {
    "x-app-id": NUTRIONIX_APP_ID,
    "x-app-key": NUTRIONIX_API_KEY,
}

nutrionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTRIONIX_ENDPOINT, json=nutrionix_params, headers=nutrionix_headers)
result = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

# Hardcoded values for testing
# exercise = result['exercises'][0]['name']
# duration =  result['exercises'][0]['duration_min']
# calories = result['exercises'][0]['nf_calories']
# body = {
#     "workout": {
#         "date": date,
#         "time": time,
#         "exercise": exercise.title(),
#         "duration": duration,
#         "calories": calories,
#     },
# }


# Dynamic values from the API response

sheety_headers = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}",
}

for exercise in result['exercises']:
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        },
    }

    # Sending the data to Sheety

response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=sheety_headers)
print(response.text)