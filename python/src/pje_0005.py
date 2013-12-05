n = 0
done = 0

while done == 0:
	n = n + 20
	
	if n % 20 == 0 and n % 19 == 0 and n % 18 == 0 and n % 17 == 0 and n % 16 == 0 and n % 14 == 0 and n % 13 == 0 and n % 11 == 0:
		done = 1

print "%d" % (n)
