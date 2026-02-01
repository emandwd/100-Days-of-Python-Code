import os
import requests
from datetime import datetime

# -----------------------Environment variables -----------------------
PIXELA_ENDPOINT = os.environ.get("PIXELA_ENDPOINT", "https://pixe.la/v1/users")
USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID", "graph1")

# ----------------------- User creation params (if needed)-----------------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ----------------------- Graph creation -----------------------
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create the graph (uncomment first time running)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#----------------------- Pixel creation -----------------------
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print("Today's date:", today.strftime("%Y-%m-%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# Create pixel (uncomment to run)
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

#----------------------- Pixel update -----------------------
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}

# Update pixel (uncomment to run)
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


#----------------------- Pixel deletion -----------------------
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Delete pixel (uncomment to run)
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
