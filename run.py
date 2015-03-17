import csv
import os
from slugify import slugify

from pymongo import MongoClient

# Connect to defualt local instance of MongoClient
client =  MongoClient()

# Get database and collection
db = client.illegaldumps
collection = db.wasteroutes

def parse():

	collection.remove({})

	print "Importing Cabrati Data"

	for filename in os.listdir('data/'):
		
		doc_count = 0
		rank = -1
		prev_lat = None
		prev_lng = None

		if(filename.endswith(".csv")):
			with open('data/' + filename, 'rb') as csvfile:
				reader = csv.reader(csvfile, delimiter = ',')
				for row in reader:
					lng = row [0]
					lat = row [1]

					if lat != 0 and lng != 0:

						if lat != prev_lat or lng != prev_lng:
							rank = rank + 1
							prev_lat = lat
							prev_lng = lng
						
						route = filename.replace('.csv', '')

						doc = {
							"lng": lng,
							"lat": lat,
							"rank": rank,
							"route": {
									"name":route,
									"slug":slugify(route)
							}
						}

						#print ("%s %s - %s")  % (lat, lng, rank) 

						collection.insert(doc) 
						doc_count = doc_count + 1

		route = filename.replace('.csv', '') 
		print ("%s documents imported from %s route")  % (doc_count, route)  					
	print "Importing finished"

parse()




						
