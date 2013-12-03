import time

start_time = time.time()

#root fibonacci numbers
a = 1
b = 2

c = 3

sum = 2

while c < 4000000:
	
	if c % 2 == 0:
		sum = sum + c
	
	a = b
	b = c
	c = a + b

elapsed_time = time.time() - start_time

print "%d found in %ss" % (sum, elapsed_time)
