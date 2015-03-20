import csv, json
import os

def dump_to_json():
	new_array = []

	for filename in os.listdir('data/'):

		if(filename.endswith(".csv")):
			with open('data/' + filename, 'rb') as csvfile:
				reader = csv.reader(csvfile, delimiter = ',')
				for row in reader:
				
					doc = {
				    	"id": 1,
				    	"imgUrl": row[5],
				    	"location":{
			          		"lat": row [1],
			          		"lng": row [2],
			    	 	},
			       		"size": row [3],
			       		"type": row [4].split(",")
			       	}

			       	print doc
			    	new_array.append(doc)

		#with open('json_datanew.json', 'w') as json_datanew:
			#json_datanew.write(new_array)
			#print new_array
dump_to_json()





		
