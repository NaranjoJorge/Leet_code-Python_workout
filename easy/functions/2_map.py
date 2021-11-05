'''
@map_to_each(func, itr): Returns list with each of the elements
in itr being apply the func function.

@func:Function that receives one and only one argument.
@itr: Iterable
'''
def map_to_each(func, itr):
	return [func(i) for i in itr]