# Uses Tweepy to communicate with Twitter API and search the stream for
# the keywords [bit ly], then filters the 'urls' field for bit.ly links
# before printing matching results

import tweepy
import yaml
import json

#API Access key variables
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Load and read from yaml file
class ConfigReader():

	def load_config(self):
		with open("conf.yml", 'r') as yml:
			conf = yaml.load(yml)
			return conf

# Listens to responses from tweepy stream
class StdOutListener(tweepy.StreamListener):

	# Prints data that contains bit.ly links
	def on_data(self, data):
		#url = data
		obj = json.loads(data)
		if 'entities' in obj and 'urls' in obj['entities'] and len(obj['entities']['urls']) > 0:
			expUrl = obj['entities']['urls'][0]['expanded_url']
			if 'http://bit.ly/' in expUrl:
				print(data)
		return True

	def on_error(self, status):
		print(status)

def readTokensFromConf():
	# We want to modify the global variables
	global access_token, access_token_secret, consumer_secret, consumer_key
	# Read tokens from config
	confReader = ConfigReader()
	config = confReader.load_config()
	access_token = config['twitter']['token']
	access_token_secret = config['twitter']['token_secret']
	consumer_key = config['twitter']['consumer_key']
	consumer_secret = config['twitter']['consumer_secret']

if __name__ == '__main__':
	# Read tokens and keys from conf
	readTokensFromConf()
	# Authenticate to Twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	# Streaming API
	listener = StdOutListener()
	stream = tweepy.Stream(auth, listener)
	stream.filter(track=['bit ly'])
