def only_until_10(x):
	#only_until_10(x): Given integer list x, returns string of numbers 0 to 10 in x.
	return ','.join(str(i)
					for i in x
					if 0 <= i <= 10)

#print(only_until_10([1,1,34,6,8]))