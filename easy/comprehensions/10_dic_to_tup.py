def dic_to_tuple(lst):
	return [(x,y) for dict in lst for x,y in dict.items()]

print(dic_to_tuple([{'Miguel':22},{'Andres':43},{'Juan':59}]))