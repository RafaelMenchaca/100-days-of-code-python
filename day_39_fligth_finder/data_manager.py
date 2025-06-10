import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    # Esta clase se encarga de hablar con Google Sheet
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            response.raise_for_status()
            print(f"{city['city']} actualizado con código {city['iataCode']}")
