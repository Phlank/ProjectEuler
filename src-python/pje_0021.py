import time
start_time = time.time()

#returns the sum of the divisors of a number
def sum_divisors(n):
	s = 0
	for i in range(1, n):
		if n % i == 0: s += i
	return s

#main
out = 0
n = 1
while n < 10000:
	n_sum = sum_divisors(n)
	n_sum_sum = sum_divisors(n_sum)
	if n == n_sum_sum and n_sum < 10000 and n != n_sum: out += n
	n += 1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
