import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from dotenv import load_dotenv

load_dotenv()  # Cargar variables desde .env

ORIGIN_CITY_IATA = "DFW"  # Puedes cambiarlo a "MEX" u otro

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Paso 1: Verifica y actualiza códigos IATA si están vacíos
sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row["iataCode"] == "":
        iata_code = flight_search.get_iata_code(row["city"])
        row["iataCode"] = iata_code
        print(f"{row['city']}: {iata_code}")
        time.sleep(3)  # Espera para evitar errores 429

data_manager.destination_data = sheet_data
data_manager.update_iata_codes()

# Paso 2: Buscar vuelos y enviar alertas si hay ofertas
for destination in sheet_data:
    flight = flight_search.search_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"]
    )

    if flight and flight.price < destination["lowestPrice"]:
        message = (
            f"💸 ¡Oferta de vuelo encontrada!\n"
            f"✈️ {flight.origin_city} → {flight.destination_city}\n"
            f"💰 Precio: ${flight.price}\n"
            f"📅 Ida: {flight.out_date} | Regreso: {flight.return_date}"
        )
        print(message)  # También lo imprimimos por consola
        notification_manager.send_message(message)
