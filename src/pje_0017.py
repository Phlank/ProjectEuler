import time
start_time = time.time()

#main
out = 0
f = open("../txt/pje_0017_nums.txt", "r")
for line in f:
	out += len(line.strip("\n"))

elapsed_time = time.time()-start_time
print "%d found in %ss" % (out, elapsed_time)
