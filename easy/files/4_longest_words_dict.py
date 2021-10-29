'''
@longest_word(file):Returns longest word in file
@file: Text file

@longest_words_dict(dir):Returns files in dir as keys and longest
word of each file as value.

@dir:Directory
'''
from json import dumps
import os

def longest_word(file):
    with open(file) as f:
        return(sorted(''.join(f).split(), key=lambda x: len(x))[-1].strip('.,:;-'))

def longest_words_dict(dir):
    d = {file: longest_word(dir+'/'+file) for file in os.listdir(dir)}
    return dumps(d,indent=4,sort_keys=True)

print(longest_word('wcfile.txt'))
print(longest_words_dict('books'))


