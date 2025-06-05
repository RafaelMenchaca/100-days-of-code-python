import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
# This is a simple habit tracker using the Pixela API.

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Habit",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2025, month=5, day=2)  # Set a specific date for testing
# print(today.strftime("%Y%m%d"))
date = today.strftime("%Y%m%d")

pixel_data = {
    "date": date,
    "quantity": "10",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
update_config = {
    "quantity": "11.5",
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)