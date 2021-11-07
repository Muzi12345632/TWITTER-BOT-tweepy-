import tweepy
import logging
import time
from config import create_api

##follow YungPluto followers
##like every tweet mention
##follow back ur followers


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



def follow_followers(api):

    logger.info("retriving followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logging.info(f"following {follower.name}")
            follower.follow()

        user = api.get_user("YungPluto2")

        print("user details")
        print(user.name)
        print(user.location)

        for follower in user.followers():
            follower.follow()

        tweets = api.mentions_timeline()
        for tweet in tweets:
            tweet.favorite()
            tweet.user.follow()


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logging.info("waiting")
        time.sleep(60)

if __name__ == '__main__':
    main()


