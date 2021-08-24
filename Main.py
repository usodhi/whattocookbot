import requests
from Food import get_random_meal
import tweepy
from tweepy.error import TweepError
from dotenv import load_dotenv
import os

# loads environment variables from .env into OS
load_dotenv('.env')
CONSUMER_API_KEY = os.getenv('CONSUMER_API_KEY')
CONSUMER_API_SECRET_KEY = os.getenv('CONSUMER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

APP_HANDLE = 'whattocookbot'

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.get_user()

def on_status(tweet):
    if APP_HANDLE in map(lambda x: x['screen_name'], tweet.entities['user_mentions']):
        meal = get_random_meal()
        # api.media_upload()

def get_image(url):
    pass

try:
    streamListener = tweepy.StreamListener(api)
    streamListener.on_connect = lambda: print("Connected!")
    streamListener.on_error = lambda error: print(error)
    streamListener.on_status = on_status

    stream = tweepy.Stream(api.auth, streamListener)
    stream.filter(track=['@whattocookbot'])

except TweepError as e:
    print(f"TweepError: \nargs:{e.api_code}\nreason:{e.reason}\nresponse:{e.response}")
