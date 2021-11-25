def flatten(x):
	return [a 
			for i in x
			for a in i
	]

#print(flatten([[1,2],[3,4]]))