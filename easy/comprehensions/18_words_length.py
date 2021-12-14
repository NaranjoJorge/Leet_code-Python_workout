def words_length(file):
	#Gets file, returns length of different words in file.
	return { len(word) for line in open(file) for word in line.split()}

#print(words_length('delfin.txt'))