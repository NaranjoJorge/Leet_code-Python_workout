
def join_numbers(x):
	#join_numbers(x): Returns numbers in range x, separated by commas.
	a = [str(i) for i in range(x)]
	return ','.join(a)

#print(join_numbers(15))