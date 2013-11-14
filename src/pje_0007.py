import time

start_time = time.time()

primes = [2, 3]
n = 3
t = 2

while t < 10001:
	n = n + 2
	i = 0
	is_prime = 1
	while i < t and is_prime == 1:
		if n % primes[i] == 0: is_prime = 0
		i = i + 1
	if is_prime == 1:
		t = t + 1
		primes.append(n)

elapsed_time = time.time() - start_time

print "%d found in %ss" % (primes[10000], elapsed_time)
		
