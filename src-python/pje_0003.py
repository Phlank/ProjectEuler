import time

start_time = time.time()

n = 600851475143
m = 2
factors = []
largest_factor = 0

while m <= n:
	
	if n % m == 0:
		n = n / m
		factors.append(m)
		if largest_factor < m: largest_factor = m
		m = 2
		
	else:
		m = m + 1
	
elapsed_time = time.time() - start_time

print "%d found in %ss" % (largest_factor, elapsed_time)
