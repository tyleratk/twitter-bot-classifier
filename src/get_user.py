import tweepy
import os
import pickle
import sys
sys.path.insert(0, '/Users/python/twitter/twitter-bot-classifier/src')
from model import BotClassifier


# ------------- set auth and initialize api -------------------------------
consumer_key = os.environ.get('twitter_consumer_key')
consumer_secret = os.environ.get('twitter_consumer_secret')
access_token = os.environ.get('twitter_access_token')
access_token_secret = os.environ.get('twitter_token_secret')


# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

with open('../models/rf.pkl', 'rb') as infile:
    model = pickle.load(infile)

user = input('Enter username: ')
# user = 'realdonaldtrump'
user_info = api.get_user(user, include_entities=1)
# import pdb; pdb.set_trace()
print(model.predict(user_info))