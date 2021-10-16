'''
@non_sense(article):Takes text file and returns nonesensical
string from the nth word on each line, where 
n is the line number.
 
@article: String
'''
def non_sense(article):
	counter = i = 0
	a = b = ''
	for line in open(article):
		line = line.split()
		while i < len(line):
			line[i] = line[i][::-1]
			i += 1
		counter += 1
		i = counter
		a = ' '.join(line)
		b += a + ' '
	return b

#print(non_sense('data.txt'))
