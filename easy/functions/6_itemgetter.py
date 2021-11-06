'''
@getitem(b): Returns f
@f(d): Returns b if b in d, otherwise returns 'b not in d'
@d:Set or dictionary
@b:String/tuple/boolean/integer or float
'''
def getitem(b):
	def f(d):
		if b in d and type(d) == dict:
			return d[b]
		elif b in d and type(d) == set:
			return b
		else: return f'{b} not in {d}'
	return f

#print(getitem(4)({1:23,2:32,3:43}))