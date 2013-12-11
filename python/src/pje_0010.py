import math

primes = [2, 3]
n = 5
t = 0

while n < 2000000:
	i = 1
	is_prime = 1
	cap = int(math.sqrt(n)) + 1
	while i < len(primes) and is_prime == 1 and primes[i] < cap:
		if n % primes[i] == 0: is_prime = 0
		i = i + 1
	if is_prime == 1: primes.append(n)
	n = n + 2
	
for p in primes:
	t = t + p
	
print "%d" % (t)
