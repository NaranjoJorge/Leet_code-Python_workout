#given a string s and an integer k, a k duplicate removal consists of choosing k 
#adjacent and equal letters from s and removing them, causing the left and the 
#right side of the deleted substring to concatenate together.

#repeatedly make k duplicate removals on s until one no longer can.
def removeDuplicates(s, k):
	i = 0
	lst = list(s)
	lst.sort()
	while i < len(lst):
		if i == len(lst) - 1:
			break
		if lst[i] == lst[i + (k-1)]:
			del lst[i:(i + k)]
			continue
		i+=1
	return ''.join(lst)