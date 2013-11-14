import time
start_time = time.time()

#main
out = 0
f = open("../txt/primes_under_one_million.txt", "r")
primes = []
for line in f:
	primes.append(int(line.strip('\n')))
k = 3
found = 0
while found == 0:
	

elapsed_time = time.time()-start_time
print '%d found in %ss' % (out, elapsed_time)
