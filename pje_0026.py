#returns the list of the first thousand decimals of a/b
#	-all trailing zeroes will be removed
#	-all repetitions following the first will be removed
def decimals(a, b):
	list = []
	t = a
	for x in range(0,1000):
		t = t%b
		list.append(t)
		t *= 10
	while list[len(list)-1] == 0:
		list.remove(len(list)-1)
	pattern = []
	for x in list:
		if pattern.count(x) == 0:
			pattern.append(x)
		else:
			for y in range(0, len(pattern)):
				if x == 
	return list
	

#main
k = decimals(1,7)
print k
