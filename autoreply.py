import tweepy
import logging
from config import create_api
import time

##tweet back to mention
##like reply tweet
##follow tweet.author

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api,keywords, since_id):

    logger.info('retrieving mentions')
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following():
                tweet.follow()

            if not tweet.favorited:
                tweet.favorite()

            api.status_update("Please reach us via DM thanks",
                             in_reply_to_status_id=tweet.id )
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "find", "missing"], since_id)
        logger.info("waiting")
        time.sleep(60)

if __name__ == '__main__':
    main()