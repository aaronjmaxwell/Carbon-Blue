"""Generate a Pre-Determined Twitter Thread.

"""
__author__ = "Aaron J. Maxwell <ajmax.85@gmail.com>"
__version__ = "0.0.3"

import configparser
import tweepy
# We use a config file to store our secret tokens so they cannot be read.
cf = configparser.ConfigParser()
cf.read('cov19thread.ini')

# We set up the OAuth Library token.
auth = tweepy.OAuthHandler(cf['AUTH']['CONSUMER_KEY'], cf['AUTH']['CONSUMER_SECRET'])
auth.set_access_token(cf['AUTH']['OAUTH_TOKEN'], cf['AUTH']['OAUTH_TOKEN_SECRET'])

# We create an API connection to Twitter.
api = tweepy.API(auth)

msg = "And can I add an image in a thread?"
message = api.update_status(status=msg)

msg = """Yes, I can, @moriartylab !"""
img = api.media_upload("/Users/ajmax/Pictures/IMG_6580.JPG")
message = api.update_status(status=msg,
                            in_reply_to_status_id=message.id,
                            auto_populate_reply_metadata=True,
                            media_ids = [img.media_id])
