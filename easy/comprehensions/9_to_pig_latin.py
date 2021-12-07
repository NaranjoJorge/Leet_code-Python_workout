def to_pig_latin(f):
	#Translate file into pig latin.
	with open(f) as r:
			lst = [word + 'way' if word[0] in 'aeiou' else word[1:] + word[0] + 'ay' for line in r for word in line.split()]
			return ' '.join(lst)

#print(to_pig_latin('amarillo.txt'))

		

		