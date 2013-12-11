import itertools

#returns the digits of l as an integer
def list_to_int(l):
        return int("".join(str(x) for x in l))

#main
out = 0
pandigitals = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
first_primes = [2, 3, 5, 7, 11, 13, 17]
for x in pandigitals:
	has_property = 1
	if list_to_int(x[1:4])%first_primes[0] != 0: has_property = 0
	elif list_to_int(x[2:5])%first_primes[1] != 0: has_property = 0
	elif list_to_int(x[3:6])%first_primes[2] != 0: has_property = 0
	elif list_to_int(x[4:7])%first_primes[3] != 0: has_property = 0
	elif list_to_int(x[5:8])%first_primes[4] != 0: has_property = 0
	elif list_to_int(x[6:9])%first_primes[5] != 0: has_property = 0
	elif list_to_int(x[7:10])%first_primes[6] != 0: has_property = 0
	if has_property == 1: out += list_to_int(x)

print "%d" % (out)
