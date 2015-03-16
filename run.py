import csv
import os
from slugify import slugify

from pymongo import MongoClient

# Connect to defualt local instance of MongoClient
client =  MongoClient()

# Get database and collection
db = client.gjakovaillegaldumps
collection = db.wasteroutes

def parse():

	collection.remove({})

	print "Importing Cabrati Data"

	for filename in os.listdir('data/'):
		truck = filename
		i = 0
		if(truck.endswith(".csv")):
			with open('data/' + truck, 'rb') as csvfile:
				reader = csv.reader(csvfile, delimiter = ',')
				for row in reader:
					longitude = row [0]
					latitude = row [1]
					truck = truck.replace('.csv', '')

					doc = {
						"longitude": longitude,
						"latitude": latitude,
						"truck": {
								"name":truck,
								"slug":slugify(truck)
						}
					}
					collection.insert(doc)
					i = i+1
		truck = truck.replace('.csv', '') 
		print ("%s documnets imported from %s truck")  % (i, truck)  					
	print "Importing finished"
parse()



						
