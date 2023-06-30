from tweetCollector import Tweets
from selenium import webdriver

username = input("Which user's tweets do you want to collect? : ")
browser = webdriver.Firefox()
bot = Tweets(username, browser)
bot.collector()