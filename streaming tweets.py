import tweepy
import json

##look for tweets containing keywords

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}: {tweet.text}")

    def on_error(self, status):
        print("error detected")

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
tweets_listner = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listner)
stream.filter(track=["find", "missing", "help"], languages=["en"])
