import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth # to use basic HTTP authentication (username/password) when making requests.

load_dotenv(dotenv_path=r"/PYTHON 100 DAYS\PYTHON COURSE DAY 39\Flight Deal Finder (Capstone Part 1)\.env")

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class DataManager: # Constructor
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json = new_data,
                auth=self._authorization,
            )
            print(response.text)