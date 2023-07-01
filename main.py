from tweetCollector import TwitterBot
from selenium import webdriver

username = "likeaseyfo"
password = "11585816252twitter"

bot = TwitterBot(username, password)
bot.login()
bot.collector("search_username")
bot.close_browser()

# Access collected tweets
print(bot.tweets)