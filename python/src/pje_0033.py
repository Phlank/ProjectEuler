#returns i as a list of digits
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

#returns a list of the factors of i
def list_factors(i):
	factors = []
	m = 2
	while m <= i:
		if i%m == 0:
			i /= m
			factors.append(m)
		else: m += 1
	return factors

#returns the numerator of the fraction a/b in lowest terms
def simplify_numer(a, b):
	numerator_factors = list_factors(a)
        denominator_factors = list_factors(b)
        product = 1
        for x in denominator_factors:
                if numerator_factors.count(x) > 0:
			numerator_factors.remove(x) 
	for x in numerator_factors:
                product *= x
        return product

#returns the denominator of the fraction a/b in lowest terms
def simplify_denom(a, b):
	numerator_factors = list_factors(a)
	denominator_factors = list_factors(b)
	product = 1
	for x in numerator_factors:
		if denominator_factors.count(x) > 0:
			denominator_factors.remove(x)
	for x in denominator_factors:
		product *= x
	return product

a = 10
out = 0
numers = []
denoms = []
numerator = 1
denominator = 1
#find the non-trivial fractions
while a < 99:
	a += 1
	b = a+1
	if a%10 == 0:
		a += 1
		b += 1
	a_list = int_to_list(a)
	while b < 100:
		if b%10 == 0: b += 1
		b_list = int_to_list(b)
		div = (a + 0.0)/b
		if a_list[0] == b_list[0] and (a_list[1]+0.0)/b_list[1] == (a+0.0)/b:
			numers.append(a_list[1])
			denoms.append(b_list[1])
		elif a_list[0] == b_list[1] and (a_list[1]+0.0)/b_list[0] == (a+0.0)/b:
			numers.append(a_list[1])
			denoms.append(b_list[0])
		elif a_list[1] == b_list[0] and (a_list[0]+0.0)/b_list[1] == (a+0.0)/b:
			numers.append(a_list[0])
			denoms.append(b_list[1])
		elif a_list[1] == b_list[1] and (a_list[0]+0.0)/b_list[0] == (a+0.0)/b:
			numers.append(a_list[0])
			denoms.append(b_list[0])
		b += 1
#simplify denominator
for x in numers:
	numerator *= x
for x in denoms:
	denominator *= x
out = simplify_denom(numerator, denominator)

print "%d" % (out)
