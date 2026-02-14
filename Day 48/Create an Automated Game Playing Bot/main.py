from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(5)

try:
    language_chosen= driver.find_element(By.ID,'langSelect-EN')
    language_chosen.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

sleep(5)

cookie= driver.find_element(By.ID, 'bigCookie')

# Every 5 seconds, check if we can buy something — keep doing that until 5 minutes have passed.”
check_interval = 5 # 5 seconds
run_duration = 5 * 60 # 5 minutes
next_check_time = time() + check_interval
end_time = time() + run_duration

while True:
    for _ in range(100):
        cookie.click()
    # Every 5 seconds, try to buy item we can afford
    if time() > next_check_time:
        try:
            cookies_element= driver.find_element(By.ID, 'cookies')
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']") # find_element() → finds one element. find_elements() → finds all elements (returns a list)
            best_item = None
            for product in reversed(products): # start with the most expensive item
                if "enabled" in product.get_attribute("class"):
                    # If this product’s class includes the word ‘enabled’, then it’s something I can buy right now.
                    best_item = product
                    break #stops the loop immediately.
            if best_item:
                best_item.click()
        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie items")
            break

    next_check_time = time() + check_interval

    if time() > end_time:
            try:
                cookies_element = driver.find_element(By.ID, 'cookies')
                print(f"Final result: {cookies_element.text}")

            except (NoSuchElementException, ValueError):
                print("Couldn't find cookie count or items")
            break





