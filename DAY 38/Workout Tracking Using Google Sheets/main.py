import os
import requests
from datetime import datetime

# ------------------------- User info (not secret) ------------------------
Gender = "female"
Weight = "58"
Height = "158"
Age = "19"

# ------------------------- Credentials / secrets -------------------------
YOUR_USERNAME = os.environ.get("SHEETY_USERNAME")
YOUR_PASSWORD = os.environ.get("SHEETY_PASSWORD")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
sheet_endpoint = os.environ.get("SHEETY_ENDPOINT")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# ------------------------- User input -------------------------
exercise_text = input("Tell me which exercise you did:  ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": Gender,
    "weight_kg": Weight,
    "height_cm": Height,
    "age": Age,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_data = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for each_one in result["exercises"]:
    sheet_inputs = {
       "sheet1": {
            "date": today_data,
            "time": now_time,
            "exercise": each_one["user_input"].title(),
            "duration": each_one["duration_min"],
            "calories": each_one["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,
                                   auth=(YOUR_USERNAME, YOUR_PASSWORD))
    print(sheet_response.text)
