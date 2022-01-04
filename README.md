# TWITTER-BOT-tweepy-

[![PyPI version](https://badge.fury.io/py/TwitterFollowBot.svg)](https://badge.fury.io/py/TwitterFollowBot)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)

A Python bot that automates several actions on Twitter, such as following users , favoriting tweets,
replying to tweet mentions and following  back followers

## Installation

You can install the Twitter Follow Bot using `pip`:

    pip install TwitterFollowBot
    pip install autoreply
    pip install like & retweet
    pip install follow followers
    pip install streaming tweets

## Dependencies

You will need to install Python's [python-twitter](https://github.com/sixohsix/twitter/) library:

    pip install twitter
    pip install tweepy

Although this library should be installed along with the Twitter Follow Bot if you used `pip`.

You will also need to create an app account on https://dev.twitter.com/apps

1. Sign in with your Twitter account
2. Create a new app account
3. Modify the settings for that app account to allow read & write
4. Generate a new OAuth token with those permissions

### Configuring the bot

Before running the bot, you must first set it up so it can connect to the Twitter API. Create a config.txt file and fill in the following information:

    OAUTH_TOKEN:
    OAUTH_SECRET:
    CONSUMER_KEY:
    CONSUMER_SECRET:
    TWITTER_HANDLE:
    ALREADY_FOLLOWED_FILE:already-followed.txt
    FOLLOWERS_FILE:followers.txt
    FOLLOWS_FILE:following.txt
    USERS_KEEP_FOLLOWING:
    USERS_KEEP_UNMUTED:
    USERS_KEEP_MUTED:
    FOLLOW_BACKOFF_MIN_SECONDS:10
    FOLLOW_BACKOFF_MAX_SECONDS:60
    
`OAUTH_TOKEN`, `OAUTH_SECRET`, `CONSUMER_KEY`, `CONSUMER_SECRET` are your API keys that you received from creating your app account. `TWITTER_HANDLE` is your Twitter name, case-sensitive.

You can change the `FILE` entries if you want to store that information in a specific location on your computer. By default, the files will be created in your current directory.

Add comma-separated Twitter user IDs to the `USERS_KEEP` entries to:

* `USERS_KEEP_FOLLOWING`: Keep following these users even if they don't follow you back.

* `USERS_KEEP_UNMUTED`: Keep these users unmuted (i.e., you receive a mobile notification when they tweet)

* `USERS_KEEP_MUTED`: Keep these users muted (i.e., you don't receive a mobile notification when they tweet)



### Syncing your Twitter following locally

Due to Twitter API rate limiting, the bot must maintain a local cache of all of your followers so it doesn't use all of your API time looking up your followers. It is highly recommended to sync the bot's local cache daily:

    from TwitterFollowBot import TwitterBot
    
    my_bot = TwitterBot()
    my_bot.sync_follows()
    
The bot will create cache files where you specified in the configuration file.
    
**DO NOT** delete the cache files ("followers.txt", "follows.txt", and "already-followed.txt" by default) unless you want to start the bot over with a fresh cache.


