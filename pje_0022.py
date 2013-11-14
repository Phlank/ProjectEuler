import time
start_time = time.time()

#main
out = 0
names = []
f = file("pje_0022_names.txt", "r")
for line in f:
	line = line.strip('\n')
	names.append(line)
names = sorted(names)
i = 0
for name in names:
	i += 1
	value = 0
	for c in name:
		value += ord(c)-64
	value *= i
	out += value

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
