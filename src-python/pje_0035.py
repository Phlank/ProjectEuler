import time
start_time = time.time()

#returns a list of digits of i
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

#returns a number from a list of digits l
def list_to_int(l):
	return int("".join(str(x) for x in l))

#returns the next 'turn' of an integer i, i.e. 1345 --> 5134 --> 4513 --> 3451
def turn(i):
	i_list = int_to_list(i)
	back = i_list.pop()
	i_list.insert(0, back)
	i = list_to_int(i_list)
	return i

#returns a list of primes up to i
def primes_list_limit(i):
	primes = [2, 3]
	found = 2
	if i < 2: return []
	if i == 2: return [2]
	k = 5
	while k < i:
		is_prime = 1
		x = 1
		while x < found and is_prime == 1 and k/primes[x] >= 3:
			if k % primes[x] == 0: is_prime = 0
			x += 1
		if is_prime == 1:
			primes.append(k)
			found += 1
		k += 2
	return primes

#main
out = 0
f = open("../txt/primes_under_one_million.txt", "r")
primes = []
for line in f:
	stripped = line.strip("\n")
	stripped = int(stripped)
	primes.append(stripped)
f.close()
for x in primes:
	y = turn(x)
	turns_are_prime = 1
	while x != y and turns_are_prime == 1:
		if primes.count(y) == 0:
			turns_are_prime = 0
		y = turn(y)
	if turns_are_prime == 1:
		out += 1
		print x

elapsed_time = time.time()-start_time
print "%d found in %ss" % (out, elapsed_time)
