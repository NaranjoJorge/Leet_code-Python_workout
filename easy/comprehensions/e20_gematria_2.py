from e19_gematria import gematria

GEMATRIA = gematria()

def gematria_for(word):
	return sum(GEMATRIA.get(letter, 0) for letter in word)

def gematria_equal_words(chars):
	return [letters.strip() for letters in open('amarillo.txt') if gematria_for(chars) == gematria_for(letters)]

#print(gematria_equal_words('del'))