import time

start_time = time.time()

primes = [2, 3]
counts = [1, 0]
n = 3

while len(primes) < 10001:
	
	n = n + 2
	is_prime = 1
	
	for i in range(1, len(counts) - 1):
		counts[i] = counts[i] + 1
		if counts[i] == primes[i]:
			counts[i] = 0
			is_prime = 0
			
	if is_prime == 1:
		primes.append(n)
		counts.append(0)

elapsed_time = time.time() - start_time

print "%d found in %ss" % (primes[10000], elapsed_time)
