n = 0		#num to test
sum = 0		#sum of successful tests

#main loop
while n < 1000:
	
	#if n is divisible by 3 or 5, add to the sum
	if n % 3 == 0 or n % 5 == 0:
		sum = sum + n
	
	#n increments
	n = n + 1

print "%d" % (sum)
