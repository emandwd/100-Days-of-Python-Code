from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

#https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=live_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

price_element = soup.find(class_="aok-offscreen")
if price_element is None:
    print("Price not found.")
    exit()

price = float(price_element.get_text().replace("$", "").strip())

#https://docs.python.org/3/library/smtplib.html
title = soup.find(id="productTitle", class_="a-size-large product-title-word-break").get_text()
title = " ".join(title.split())
#print(repr(title))

BUY_PRICE = 100

load_dotenv()
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD= os.environ.get("EMAIL_PASSWORD")

if price < BUY_PRICE:
    message =  f"{title} is on sale for {price}!"
    print(message)
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode("utf-8")
        )




