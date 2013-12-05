import math

#transforms an integer to a list of separate digits
def int_to_list(i):
	list = [int(x) for x in str(i).zfill(1000)]
	while list[0] == 0: list.remove(0)
	return list

out = 0
digits = int_to_list(math.factorial(100))
for x in digits: out += x

print "%d" % (out)
