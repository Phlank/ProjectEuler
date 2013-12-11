out = 0
a = 2
b = 2
nums = []
while a <= 100:
	b = 2
	while b <= 100:
		temp = a**b
		if nums.count(temp) == 0:
			nums.append(temp)
			out += 1
		b += 1
	a += 1

print "%d" % (out)
