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

print "%d" % (largest_factor)
