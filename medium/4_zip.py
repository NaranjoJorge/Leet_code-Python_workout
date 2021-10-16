'''
@zip(*iterables): Emulates built-in zip(). Returns list of tuples.
Each tuple will contain one element from each of the iterables passed.

@*iterables: Iterables.
'''
from operator import itemgetter

def zip(*iterables):
	a = []
	for i in range(len(iterables[0])):
		a.append(tuple(map(itemgetter(i), iterables)))
	return a

#print(zip([10,20,30], 'abc'))

