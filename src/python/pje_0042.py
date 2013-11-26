import time
start_time = time.time()

#main
MIN = ord('A')-1
f = open("../../txt/pje_0042_words.txt", "r")
triangles = []
out = 0
for x in range(1, 1000):
	triangles.append(x*(x+1)/2)
for line in f:
	line = line.strip('\n')
	line_sum = 0
	for c in line: line_sum += ord(c)-MIN
	if triangles.count(line_sum) > 0: out += 1
f.close()

elapsed_time = time.time()-start_time
print "%d found in %ss" % (out, elapsed_time)
