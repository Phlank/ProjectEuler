import time
start_time = time.time()

#returns list of first k prime numbers
def list_primes(k):
	primes = [2, 3]
	if k < 1: return []
	elif k == 1: return [2]
	elif k == 2: return [2, 3]
	else:
		n = 3
		t = 2
		while t < k+1:
			n += 2
			i = 0
			is_prime = 1
			while i < t and is_prime == 1:
				if n%primes[i] == 0: is_prime = 0
				i += 1
			if is_prime == 1:
				t += 1
				primes.append(n)
		return primes

#returns list of all primes less k
def list_primes_limit(k):
	primes = [2, 3]
	if k < 3: return []
	elif k == 3: return [2]
	elif k == 4: return [2, 3]
	else:
		n = 5
		t = 2
		while n < k:
			i = 0
			is_prime = 1
			while i < t and is_prime == 1:
				if n%primes[i] == 0: is_prime = 0
				i += 1
			if is_prime == 1:
				t += 1
				primes.append(n)
			n += 2
		return primes

#returns the output of the quadratic function given in the problem
def q_function(n, a, b):
	return n**2+a*n+b

#main
out = 0
primes = list_primes(1000)
a = -1000
b = -1000
n = 0
top_count = 0
while a < 1000:
	b = 0
	while b < 1000:
		count = 0
		n = 0
		while primes.count(q_function(n, a, b)) == 1:
			count += 1
			n += 1
		if top_count < count:
			top_count = count
			out = a*b
		b += 1
	a += 1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
