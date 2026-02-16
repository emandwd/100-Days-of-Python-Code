from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys


#----------------------------------------------------------------------------------------------------------------------

PROMISED_DOWN = 150
PROMISED_UP = 10

load_dotenv()

TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
URL = os.environ.get("SPEEDTEST_URL")

#---------------------------------------------------------------------------------------------------------------------

class InternetSpeedTwitterBot:
    def __init__(self, driver_path=None):
        chrome_options = uc.ChromeOptions()
        self.up = 0
        self.down = 0

        prefs = {
            "profile.default_content_setting_values.geolocation" : 1 # 1=allow, 2=block, 0=ask
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-service-autorun")
        chrome_options.add_argument("--password-store=basic")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")

        self.driver = uc.Chrome(options=chrome_options)



    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(4)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text" )
        go_button.click()
        print("Running speed test...")
        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        print("Down:", self.down)
        print("Up:", self.up)

    def tweet_at_provider(self):
        print("Opening Twitter login...")
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        try:
            # Login
            username_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            username_input.send_keys("username_input")
            username_input.send_keys(Keys.ENTER)
            time.sleep(3)

            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5)

            Content = f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

            try:
                # Wait for the tweet box to be clickable
                post_content = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']"))
                )

                # Optional: Close popups that may block the tweet box
                try:
                    not_now = self.driver.find_element(By.XPATH,
                                                       "//span[text()='Not now']/ancestor::div[@role='button']")
                    not_now.click()
                    time.sleep(1)
                except:
                    pass

                # Click and type the tweet
                post_content.click()
                print("Writing post...")
                post_content.send_keys(Content)
                print(f"POST: {Content}")

                # CTRL + ENTER to send
                post_content.send_keys(Keys.CONTROL, Keys.ENTER)
                time.sleep(3)
                print("Tweet sent successfully!")

            except Exception as e:
                print("❌ Failed to post tweet:", e)

        except Exception as e:
            print("❌ Failed to post tweet:", e)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

# Keep the browser open
input("Press Enter to close the browser...")

