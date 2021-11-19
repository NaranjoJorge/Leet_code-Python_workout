def backwards(file):
	#Given a file, returns a list that contains the words in the file,
	#only that in the opposite order of file. Hence first word of the file would be
	#last word of list and viceversa.
	with open(file) as f:

		return [' '.join(line.split()[::-1]) for line in f if len(line) > 1]

#print(backwards('amarillo.txt'))