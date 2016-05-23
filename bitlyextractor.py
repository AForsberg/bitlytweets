# Communicates with bitly.com to expand short URL's

import yaml
from bitlyapipython import bitly_api

# Load and read from yaml file
class ConfigReader():

	def load_config(self):
		with open("conf.yml", 'r') as yml:
			conf = yaml.load(yml)
			return conf

# Set up API auth
confReader = ConfigReader()
config = confReader.load_config()
login = config['bitly']['login']
api_key = config['bitly']['api_key']
generic_token = config['bitly']['generic_token']

# File to write to
o = open('../data/expanded.txt', 'a')

# Open connection
c = bitly_api.Connection(access_token=generic_token)

# Send request to bitly API and write response to file.
# shortUrls is an array of up to 15 short URL's (bitly.com API max limit)
def expandShortUrl(shortUrls):
	response = c.expand(shortUrl=shortUrls)
	o.write(str(response) + '\n')