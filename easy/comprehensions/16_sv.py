def get_sv(file):
	#Recieves file and returns set of supervocalic words in the file.
	vowels = {'a','e','i','o','u'}
	return {line.strip() for line in open(file) if vowels < set(line.lower())}

#print(get_sv('/Users/jorgenaranjo/Documents/words.txt'))