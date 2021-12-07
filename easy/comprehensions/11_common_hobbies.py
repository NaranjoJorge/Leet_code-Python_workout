from operator import itemgetter

def common_hobbies(lst):
	#Given a lst of dicts. Where dicts have two key(name & hobbies)-value pairs. Hobbies is a set of
	#strings. Returns three most popular hobbies among people listed.
	hobbies = [hobbie for dict in lst for hobbie in dict['Hobbies']]
	h_tuple = [(i, hobbies.count(i)) for i in hobbies]
	hobbies = sorted(list(set(h_tuple)), key=itemgetter(1), reverse=True)
	hobbies = [tup[0] for tup in hobbies]
	return hobbies[:3]


print(common_hobbies([{'Name':'Miguel', 'Hobbies': {'Polo','Soccer'}},{'Name':'Juan', 'Hobbies':{'Basket', 'Volleyball', 'Polo'}},{'Name':'Andres', 'Hobbies':{'Polo','Volleyball','Swimming'}}]))