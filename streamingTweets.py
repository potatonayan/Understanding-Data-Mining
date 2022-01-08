from tweepy import Stream, auth
from tweepy import StreamListener
import tweepy
import twitterCredentials

auth = auth.OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
auth.set_access_token(twitterCredentials.ACCESS_TOKEN,twitterCredentials.ACCESS_SECRET)

api = tweepy.API(auth)
class MyListener(StreamListener):
    def on_data(self, raw_data):
        try:
            with open('python.txt', 'a') as f:
                f.write(raw_data)
                return True
        except BaseException as e:
            print('Error on_data: %s' % str(e))
        return True

    def on_error(self, status_code):
        print(status_code)
        return True

twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=['#dogecoin'])

