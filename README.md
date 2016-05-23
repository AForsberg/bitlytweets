# bitly-tweets
Small python tools that searches for tweets containing bitly links and expands the original URL's. 

Uses pip packages Tweepy and bitly_api.

Looks for a file called 'conf.yml' for API authentication keys.

## bitly-tweets-finder.py
Authenticates to Twitter and searches for tweets using the Streaming API and prints any tweets containing bit.ly links to console.

## bitly-tweets-datahandler.py
Loads tweets from file, parses to JSON and calls bitlyextractor.py for URL expansion.

### bitlyextractor.py
Authenticates to Bitly and expands the URL's passed to it by bitly-tweets-datahandler, writes the results to file. 

## bitly-tweets-urlhandler.py
Compares the expanded URL's against a given .csv file of malicious domains. Prints any matching domains to console.  
