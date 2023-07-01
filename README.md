# TwitterBot - Tweet Collector

This project is a Python script that utilizes Selenium and the Firefox WebDriver to log into Twitter, search for a specific user, and collect all their tweets.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Selenium library (`pip install selenium`)
- Mozilla Firefox browser

## Setup

1. Clone the repository or download the script files (`tweetCollector.py` and `main.py`) to your local machine.

2. Install the required dependencies by running the following command:

   ```shell
   pip install selenium
   ```

3. Set your Twitter username and password in the `main.py` script:

   ```python
   username = "your_username"
   password = "your_password"
   ```

4. Customize the search by modifying the parameter passed to the `bot.collector()` method in the `main.py` script. Replace `"search_name"` with the username of the Twitter account you want to collect tweets from.

## Usage

To run the script and collect tweets, execute the following command:

```shell
python main.py
```

The script will open a Firefox browser window, log into Twitter using your provided credentials, search for the specified user, and start collecting their tweets. The collected tweets will be stored in the `bot.tweets` list.

## Accessing Collected Tweets

After the script finishes running, you can access the collected tweets by printing the `bot.tweets` list. Modify the `main.py` script as follows:

```python
# Access collected tweets
for tweet in bot.tweets:
    print(tweet)
```

Save the changes and run the script again.

## Limitations

- Twitter's website structure and CSS class names may change over time, causing the script to fail. If that happens, you may need to update the CSS selectors in the `tweetCollector.py` script to match the updated website structure.

- The script waits for a fixed amount of time between actions (e.g., clicking buttons, scrolling). Adjust the sleep durations in the `tweetCollector.py` script if needed to accommodate slower internet connections or different website loading speeds.

- This script only collects the visible tweets on the page. If the user has a large number of tweets, it may not capture all of them. Consider modifying the script to load more tweets by scrolling further down the page if needed.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and respect Twitter's terms of service.
