from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os


practice_url= "https://appbrewery.github.io/Zillow-Clone/"

#https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Device-Memory": "8",
    "Downlink": "9.85",
    "DPR": "1.5",
    "ECT": "4g",
    "Priority": "u=0, i",
    "Referer": "https://www.google.com/",
    "RTT": "100",
    "Sec-CH-Prefers-Color-Scheme": "light",
    "Sec-CH-Prefers-Reduced-Motion": "no-preference",
    "Sec-CH-UA": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    "Sec-CH-UA-Arch": "x86",
    "Sec-CH-UA-Full-Version": '"140.0.7339.208"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Model": '""',
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-CH-UA-Platform-Version": '"19.0.0"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Viewport-Width": "1280"
}

list_link = []
list_price = []
list_address = []

response = requests.get(url=practice_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

# Create a list of all the links on the page using a CSS Selector

all_links = soup.find_all('a', class_="property-card-link")
for link in all_links:
    list_link.append(link.get('href'))
print(list_link)

# Create a list of prices for all the listings you scraped

prices = soup.find_all("span", {"data-test": "property-card-price"})
for price in prices:
    clean_price = re.sub(r'[^\d]', '', price.text)
    list_price.append(f"${clean_price}")
print(list_price)

#Create a list of addresses for all the listings you scraped.

addresses = soup.find_all('a', class_="StyledPropertyCardDataArea-anchor" )
for address in addresses:
    clean_address = address.text.strip() # .strip() removes leading/trailing spaces, newlines, and tabs
    list_address.append(clean_address)
print(list_address)

# Fill in the Google Form using Selenium

load_dotenv()
URL = os.environ.get("GOOGLE_FORM_URL")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(list_link)):
    driver.get(url=URL)
    time.sleep(2)
    address=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price=driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(list_address[n])
    price.send_keys(list_price[n])
    link.send_keys(list_link[n])
    submit_button= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()






