from tweetCollector import TwitterBot
from selenium import webdriver

username = "your_username"
password = "your_password"

bot = TwitterBot(username, password)
bot.login()
bot.collector("search_name")
bot.close_browser()

# Access collected tweets
print(bot.tweets)