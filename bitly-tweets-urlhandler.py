# Compares the URL's in urlPath against the lists
# domains.csv and malwaredomains.csv
# Prints the matching links.

import json
import csv
from urllib.parse import urlparse

# JSON formatted responses from bitly, 15 per line
urlPath = '../data/expanded.txt'
domainListPathOne = '../data/DomainList/domains.csv'
domainListPathTwo = '../data/DomainList/malwaredomainlist.csv'

urlData = []
urlsArray = []
urlsJson = []

malicious = []

if __name__ == '__main__':


	urlFile = open(urlPath, 'r')

	# Load data from expanded.txt, will be 15 urls per json object.
	for line in urlFile:
		try:
			urlData.append(line)
		except:
			continue

	# Each 15-url json obj
	for obj in urlData:
		obj = obj.replace("'", '"')
		try:
			jsonUrl = json.loads(obj)
			urlsJson.append(jsonUrl)
		except:
			continue

	for url in urlsJson:
		for o in url:
			if 'long_url' in o:
				urlsArray.append(o['long_url'])


	with open(domainListPathOne, newline='', encoding='ISO-8859-1') as csvfile:
		domainReader = csv.reader(csvfile, delimiter='\t')
		try:
			for row in domainReader:
				if len(row) > 2:
					malicious.append(row[2])
		except csv.Error as e:
			print(e)

	with open(domainListPathTwo, newline='', encoding='ISO-8859-1') as csvfile:
		domainReader = csv.reader(csvfile, delimiter=',')
		try:
			for row in domainReader:
				if len(row) > 2:
					s = '//' + str(row[1])
					o = urlparse(s)
					malicious.append(o[1])
		except csv.Error as e:
			print(e)

	totalMatches = []
	for item in malicious:
		if item == '-' or item == 'domain' or item == 'notice':
			continue
		matches = [m for m in urlsArray if item in m]
		if len(matches) > 0:
			print(item + ' - Found links containing: ')
			print(matches)
