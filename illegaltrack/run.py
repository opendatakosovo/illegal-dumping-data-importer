import csv, json
import os

def dump_to_json():
    
    for filename in os.listdir('data/'):

        if(filename.endswith(".csv")):
            with open('data/' + filename, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter = ',')

                new_array = []

                for row in reader:

                    doc = {
                        "id": 1,
                        "imgUrl": row[4],
                        "location":{
                            "lat": float(row[0]),
                            "lng": float(row[1]),
                        },
                        "size": row[2],
                        "type": row[3].split(",")
                    }


                    new_array.append(doc)

                print new_array

        #with open('json_datanew.json', 'w') as json_datanew:
            #json_datanew.write(new_array)
            #print new_array
dump_to_json()





        
