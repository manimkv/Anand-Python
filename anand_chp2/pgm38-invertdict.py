# Program to invert a dictionary with unique values

def invertdict(d):
	dict={}
	for k,v in d.items():
		dict[v]=k
	return dict
print invertdict({'x': 1, 'y': 2, 'z': 3})
