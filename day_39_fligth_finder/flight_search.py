import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData
from datetime import datetime, timedelta

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.token = self.get_token()

    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_iata_code(self, city_name):
        url = f"https://test.api.amadeus.com/v1/reference-data/locations?keyword={city_name}&subType=CITY"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        results = response.json()["data"]

        for result in results:
            if result["subType"] == "CITY":
                return result["iataCode"]

        return None


    def search_flights(self, origin_city_code, destination_city_code):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        six_months_later = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": tomorrow,
            "returnDate": six_months_later,
            "adults": 1,
            "currencyCode": "USD",
            "max": 1
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        try:
            flight = data["data"][0]
            price = float(flight["price"]["total"])
            itinerary = flight["itineraries"][0]["segments"][0]
            return_itinerary = flight["itineraries"][1]["segments"][0]

            return FlightData(
                price=price,
                origin_city=itinerary["departure"]["iataCode"],
                origin_airport=itinerary["departure"]["iataCode"],
                destination_city=itinerary["arrival"]["iataCode"],
                destination_airport=itinerary["arrival"]["iataCode"],
                out_date=itinerary["departure"]["at"].split("T")[0],
                return_date=return_itinerary["arrival"]["at"].split("T")[0]
            )
        except (KeyError, IndexError):
            print(f"No flights found for {destination_city_code}.")
            return None
