'''
@diffdict(first, second): Returns new dict with values
that are different between first & second dicts.

@first: Dictionary
@second: Dictionary
'''
def diffdict(first, second):
	new = {}
	k = set()

	for key in first.keys():
		k.add(key)
	for key in second.keys():
		k.add(key)
	
	for key in k:
		if first.get(key) != second.get(key):
			new[key] = [first.get(key), second.get(key)]
	return new

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'd':4}
#print(diffdict(d1, d2))


