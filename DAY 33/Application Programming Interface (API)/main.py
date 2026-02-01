import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# print(response) --> output : <Response [200]> --> this is the response code

response.raise_for_status()  # Instead of using if-else for each HTTP status code, as shown in: https://www.webfx.com/web-development/glossary/http-status-codes/

data = response.json() # .json() is a method that reads the response body and tries to convert (deserialize) it from JSON format into a Python object( Python dictionary )

# print(data) -->  output : {'message': 'success', 'timestamp': 1754699353, 'iss_position': {'longitude': '-120.3431', 'latitude': '23.8230'}}

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print((longitude, latitude))
