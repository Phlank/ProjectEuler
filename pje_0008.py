import fileinput
import time

start_time = time.time()

maximum = 0
f = open("pje_0008_n.txt", "r")
n = f.read()
i = 0
j = len(n) - 5

while i < j:
	product = 1
	for k in xrange(i, i+5): product = product * int(n[k])
	if maximum < product: maximum = product
	i = i + 1

elapsed_time = time.time() - start_time

print "%d found in %ss" % (maximum, elapsed_time)
