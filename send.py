 # importing the module
"""
 Build and Tweet
"""

import os
import csv
import time
import tweepy

# personal details
consumer_key = os.getenv('c_key')
consumer_secret = os.getenv('c_secret')
access_token = os.getenv('a_token')
access_token_secret = os.getenv('a_secret')
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_offset(i):
    return (int(i) * 60)

with open('commentary-log.csv') as csvfile:
 reader = csv.DictReader(csvfile)
 for row in reader:
    time.sleep(get_offset(row['offset']))
    # update the status
    api.update_status(status = row['text'])

