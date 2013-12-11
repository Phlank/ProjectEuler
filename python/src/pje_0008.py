maximum = 0
f = open("../../txt/pje_0008_n.txt", "r")
n = f.read()
i = 0
j = len(n) - 5

while i < j:
	product = 1
	for k in xrange(i, i+5): product = product * int(n[k])
	if maximum < product: maximum = product
	i = i + 1

print "%d" % (maximum)
