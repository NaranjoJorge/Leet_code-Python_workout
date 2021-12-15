import json

def json_dict(file):
	#Makes dict from jason file.
	return {value["city"]:value["population"] for value in json.load(open(file))}

#print(json_dict('cities.json'))

def json_key_tuple(file):
	#Makes dict from jason file.
	return {(value["state"],value["city"]):value["population"] for value in json.load(open(file))}

#print(json_key_tuple('cities.json'))

