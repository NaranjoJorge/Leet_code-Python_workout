def inside_out(d):
	#Keys and values in d are reversed.
	return {v:k for k,v in d.items()}

#print(inside_out({'a':1, 'b':2}))