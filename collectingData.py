import tweepy
from tweepy import OAuthHandler
from tweepy.models import Friendship
import simplejson as json
import twitterCredentials
def process_or_store(tweet):
    print(json.dumps(tweet))
    print()

auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
auth.set_access_token(twitterCredentials.ACCESS_TOKEN,twitterCredentials.ACCESS_SECRET)

api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(10):
#   process_or_store(status._json)
    

#for tweet in tweepy.Cursor(api.user_timeline).items():
#    process_or_store(tweet._json)

for status in tweepy.Cursor(api.friends).items():
    process_or_store(status._json)