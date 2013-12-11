a, b, c = 1, 2, 3
a_t, b_t, c_t = 1, 1, 1
done = 0
product = 0

while c < 1000 and done == 0:
	b = 2
	while b < c and done == 0:
		a = 1
		while a < b and done == 0:
			if a + b + c == 1000:
				test = a**2 + b**2
				if test == c**2:
					done = 1
					product = a * b * c
					a_t, b_t, c_t = a, b, c
			a = a + 1
		b = b + 1
	c = c + 1

print "%d" % (product)
