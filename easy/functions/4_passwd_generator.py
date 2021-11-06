'''
@passwd_generator(b): Enclosing fuction. 
@nested(a): Returns password with size a from combination
of elements in b.

@b: String
@a: Integer
'''
import random

def passwd_generator(b):
	def nested(a):
		passwd = ''
		for i in range(a):
			passwd += random.choice(b)
		return passwd
	return nested

#print(passwd_generator('america$?')(4))
