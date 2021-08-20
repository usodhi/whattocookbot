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

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    pass
except TweepError as e:
    print(f"TweepError: \nargs:{e.api_code}\nreason:{e.reason}\nresponse:{e.response}")