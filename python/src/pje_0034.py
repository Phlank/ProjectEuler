#returns an integer as a list of digits
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

#returns i!
def factorial(i):
	if i < 1: return 1
	product = 1
	while i > 1:
		product *= i
		i -= 1
	return product

#returns i! faster for i < 10
def small_factorial(i):
	if i < 2: return 1
	if i == 2: return 2
	if i == 3: return 6
	if i == 4: return 24
	if i == 5: return 120
	if i == 6: return 720
	if i == 7: return 5040
	if i == 8: return 40320
	if i == 9: return 362880

#returns x[1]!+x[2]!+x[3]!+...+x[n]! where x[k] are digits of i!
def digit_factorial_sum(i):
	sum = 0
	i_list = int_to_list(i)
	for x in i_list:
		sum += small_factorial(x)
	return sum

out = 0
n = 3
max = small_factorial(9)
while n < max:
	if n == digit_factorial_sum(n):
		out += n
	n += 1

print "%d" % (out)
