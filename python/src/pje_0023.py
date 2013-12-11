def sum_divisors(n):
	s = 0
	for i in range(1, n):
		if n % i == 0: s += i
	return s

def is_abundant(n):
	if n < sum_divisors(n): return 1
	else: return 0

out = 0
max = 28123
nums = []
abundant_nums = []
for i in range(1, max): nums.append(i)
for i in nums:
	if is_abundant(i): abundant_nums.append(i)
for i in range(0, len(abundant_nums)):
	for j in range(0, len(abundant_nums)):
		k = abundant_nums[i] + abundant_nums[j]
		if k < max:
			nums[k-1] = 0
for i in nums: out += i

print "%d" % (out)
