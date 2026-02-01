import requests
from datetime import datetime
import smtplib
import time
import os

""" https://www.latlong.net/ """

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))


FormattedTime = 0

def is_iss_overhead() :
    response = requests.get(url="http://api.open-notify.org/iss-now.json") # public open API
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    # We put our required parameters in a dictionary
    parameters = {
        "lat":  MY_LAT,
        "lng":  MY_LONG,
        "formatted" : FormattedTime,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params= parameters) # public open API
    response.raise_for_status()
    # Output: 400 Client Error → This means the issue is on our side.
    # If we think about it, we’ll realize it’s because we didn’t provide
    # the API with the required parameters (non-default parameters).
    data = response.json()
    # print(data) --> output : {'results': {'sunrise': '2:24:24 AM', 'sunset': '3:32:55 PM', 'solar_noon': '8:58:39 AM', 'day_length': '13:08:31', 'civil_twilight_begin': '2:01:35 AM', 'civil_twilight_end': '3:55:43 PM', 'nautical_twilight_begin': '1:33:09 AM', 'nautical_twilight_end': '4:24:10 PM', 'astronomical_twilight_begin': '1:03:55 AM', 'astronomical_twilight_end': '4:53:23 PM'}, 'status': 'OK', 'tzid': 'UTC'}
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # print(sunrise) --> 12 hour formate
    # print(sunrise)
    # print(sunset)
    """
    .split("T") means: Take the string in sunrise and break it into a list of parts wherever the letter "T" appears.
    """
    time_now = datetime.now().hour
    # print(time_now.hour) # 24 hour formate
    if time_now >= sunset or time_now <= sunrise :
        return True



while True :
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg="Subject: Look Up👆\n\nThe ISS is above you in the sky."
        )

