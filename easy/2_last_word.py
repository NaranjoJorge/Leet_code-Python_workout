#Given a string s consisting of some words separated by some number of spaces, 
#return the length of the last word in the string.

def lengthOfLastWord(s):
	return len(s.split()[-1])

