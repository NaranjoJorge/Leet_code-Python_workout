def family_tree(d):
	#Given a dictionary with Dad names as keys and their respective childs names as value, returns
	# list of children.
	return [name
					for lst in d.values()
					for name in lst
			]

#print(family_tree({'Daniel': ['Andrew', 'Walter'], 'Miguel': ['Tomas', 'Jeronimo', 'Italo']}))