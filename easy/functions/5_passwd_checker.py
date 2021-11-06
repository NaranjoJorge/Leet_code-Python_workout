'''
@passwd_checker(min_up, min_low, min_punct, min_digit): Returns nested.
@nested(b): Returns true if uppercase, lowercasse, punctuation & digits in 
b are >= to min_up, min_low, min_punct, min_digit respectively.

@min_up: Integer
@min_low: Integer
@min_punct: Integer
@min_digit: Integer
@b: String
'''
import string

def passwd_checker(min_up, min_low, min_punct, min_digit):
	def nested(b):
		if not min_up <= sum(1 for char in b if char.isupper()):
			return False
		if not min_low <= sum(1 for char in b if char.islower()):
			return False
		if not min_digit <= sum(1 for char in b if char.isdigit()):
			return False
		if not min_punct <= sum(1 for char in b if char in string.punctuation):
			return False
		return True
	return nested

#print(passwd_checker(3, 3, 3, 3)('UYXmsw123?%!'))