import string

def gematria():
	#Def returns dict where keys are lowercase alphabet letters and values are
	#numbers from 1 to 26 (being a:1, b:2, c:3, ...z:26)
	return {letter:number for number,letter in enumerate(string.ascii_lowercase,1)}

print(gematria())