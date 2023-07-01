from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TwitterBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "https://twitter.com/"
        self.tweets = []


    def login(self):
        browser = webdriver.Firefox()
        browser.get(self.url)
        time.sleep(2)

        username_field = browser.find_element(By.CSS_SELECTOR, '.r-30o5oe')
        username_field.send_keys(self.username)
        time.sleep(2)


        next_button = browser.find_element(By.CSS_SELECTOR, "div.css-18t94o4:nth-child(6) > div:nth-child(1)")
        next_button.click()
        time.sleep(2)


        password_field = browser.find_element(By.CSS_SELECTOR, '.r-homxoj')
        password_field.send_keys(self.password)
        time.sleep(2)


        login_button = browser.find_element(By.CSS_SELECTOR, '.r-19yznuf > div:nth-child(1)')
        login_button.click()
        time.sleep(2)

        self.browser = browser


    def collector(self, search_username):
        search_url = self.url + f"{search_username}"
        self.browser.get(search_url)

        time.sleep(2)

        while True:
            tweet_elements = self.browser.find_elements(By.CSS_SELECTOR, 'section.css-1dbjc4n:nth-child(3)')
            time.sleep(5)
            for tweet_element in tweet_elements:
                tweet_text_element = tweet_element.find_element(By.CSS_SELECTOR, '#id__0j5akj58zgno > span:nth-child(1)')
                tweet_text = tweet_text_element.text
                self.tweets.append(tweet_text)

            time.sleep(5)
            scrollable_div = self.browser.find_element(By.CSS_SELECTOR, '.r-urgr8i')
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
            time.sleep(3)

            new_tweet_elements = self.browser.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweet"]')
            if len(new_tweet_elements) == len(tweet_elements):
                break


    def close_browser(self):
        self.browser.quit()