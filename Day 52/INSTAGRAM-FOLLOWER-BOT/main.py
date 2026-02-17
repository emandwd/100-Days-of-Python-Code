from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

load_dotenv()

INSTAGRAM_PASS = os.getenv("INSTAGRAM_PASS")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
SIMILAR_ACCOUNT = "buzzfeedtasty"

class InstaFollower:
    def __init__(self, driver_path=None):
        chrome_options = uc.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.cookies": 1, # 1=allow, 2=block, 0=ask
            "profile.default_content_setting_values.geolocation": 1,
        }
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-service-autorun")
        chrome_options.add_argument("--password-store=basic")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")

        self.driver = uc.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        username.send_keys(INSTAGRAM_USERNAME)
        password.send_keys(INSTAGRAM_PASS)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        try:
            time.sleep(10)
            save_info = self.driver.find_element(By.CSS_SELECTOR, '.x78zum5 button')
            save_info.click()
        except:
            print("No 'Not now' popup appeared for save login info.")

        time.sleep(5)

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        followers_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
        )
        followers_btn.click()

        print("Waiting for followers list to open...")
        followers_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x6nl9eh.x1a5l9x9.x7vuprf.x1mg3h75.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(2) > div"
                                            ))
        )
        print("Followers list found!")
        self.scrollable_popup = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x6nl9eh.x1a5l9x9.x7vuprf.x1mg3h75.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6"
            ))
        )

        for i in range(10):  # scroll 20 times
            self.driver.execute_script("arguments[0].scrollTop += 300;", self.scrollable_popup)
            time.sleep(1.5)

    def follow(self):

        all_buttons = self.scrollable_popup.find_elements(By.TAG_NAME, 'button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()




if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
    input("Press Enter to close the browser...")

