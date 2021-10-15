'''
@first_last(x): Returns first and last element of
sequence in a two-element sequence of the same type.

@x: list, string or tuple
'''

def first_last(x):
	return x[:1] + x[-1:]

print(first_last([[1,2],'b','w', 'oo']))