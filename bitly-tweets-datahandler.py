# Loads tweets from file and sends in batches of 15 to bitlyextractor.py

import json
import bitlyextractor

# Path to datafile
tweetsPath = '../data/tweetsSplitaj'

# Object to hold our json data
tweetsData = []
expandedData = []

# Main method
if __name__ == '__main__':

	# Open the file
	tweetsFile = open(tweetsPath, 'r')

	# Read from file to tweetsData
	for line in tweetsFile:
		try:
			tweet = json.loads(line)
			tweetsData.append(tweet)
		except:
			continue

	nrOfTweets = len(tweetsData)
	tweets = []
	progress = 0

	# Adds tweets to tweets array, when 15 it sends to extractor
	# Prints progress after every batch sent
	for tw in tweetsData:
		tweets.append(tw['entities']['urls'][0]['expanded_url'])
		if len(tweets) == 15:
			bitlyextractor.expandShortUrl(tweets)
			tweets.clear()
			progress += 1
			print(str(round(((((progress) * 15) / nrOfTweets) * 100), 3)) , '%', end='\r')