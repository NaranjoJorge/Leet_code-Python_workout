'''
@even_odd_sum(x): Returns as list sum of even & odd 
indexed numbers.
@x: String or tuple
'''
def even_odd_sum(x):
	even_sum = odd_sum = 0
	for i in x[::2]:
		even_sum += i
	for i in x[1::2]:
		odd_sum += i
	return [even_sum,odd_sum]

#print(even_odd_sum((1,20,40)))