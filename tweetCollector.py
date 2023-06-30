from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

sleep = time.sleep(2)

class Tweets():
    def __init__(self,searchname, browser):
        self.searchname = searchname
        self.browser = browser
        self.url = "https://twitter.com/"
        self.tweets = []


    def login(self, username, password):
        self.username = username
        self.password = password
        self.browser.get(self.url)


    def collector(self):
        self.browser.get(self.url+f"{self.username}")
        sleep


