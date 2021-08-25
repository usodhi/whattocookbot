import requests
from Food import get_random_meal
import tweepy
from tweepy.error import TweepError
from dotenv import load_dotenv
import os
import sys

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

def on_status(tweet):
    if APP_HANDLE in map(lambda x: x['screen_name'], tweet.entities['user_mentions']) and tweet.in_reply_to_status_id is None:
        meal = get_random_meal()
        filename = get_image(meal['imageUrl'])
        api.update_with_media(filename, status=get_status(meal, tweet.user.screen_name), in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        os.remove(filename)
        print("Tweet complete!")

def get_image(url):
    filename = 'temp.jpg'
    r = requests.get(url, stream=True)
    if not r.status_code == 200:
        print(f"Error: could not fetch image, code {r.status_code}")
        sys.exit(1)

    try:
        with open(filename, 'wb') as image:
            for chunk in r:
                image.write(chunk)
    except Exception as e:
        print(e)
        
    return filename

def get_status(meal, reply_to_screen_name):
    name = meal['name']
    dishType = meal['dishType']
    geoLocation = meal['geoLocation']
    instructions = meal['instructions']
    ingredients = meal['ingredients']
    source = meal['source']
    videoUrl = meal['videoUrl']

    print(instructions)

    status = f'''@{reply_to_screen_name}
Name: {name}
Type: {dishType}
Location: {geoLocation}
Source: {source}
Video: {videoUrl}
    '''
    return status

try:
    streamListener = tweepy.StreamListener(api)
    streamListener.on_connect = lambda: print("Connected!")
    streamListener.on_error = lambda error: print(error)
    streamListener.on_status = on_status

    stream = tweepy.Stream(api.auth, streamListener)
    stream.filter(track=['@whattocookbot'])

except TweepError as e:
    print(f"TweepError: \nargs:{e.api_code}\nreason:{e.reason}\nresponse:{e.response}")
