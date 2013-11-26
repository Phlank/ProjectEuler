import time
start_time = time.time()

from collections import deque

#returns i as a list of digits
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0 and len(list) > 1:
		list.remove(0)
        return list

#returns a list of digits l as an integer
def list_to_int(l):
        return int("".join(str(x) for x in l))

#returns 1 if i is truncable
def is_truncable(i):
	if i == 2 or i == 3 or i == 5 or i == 7: return 0
	i_list = int_to_list(i)
	forward_i, backward_i = deque(i_list), deque(i_list)
	truncable = 1
	while len(forward_i) > 0 and truncable == 1:
		if primes.count(list_to_int(list(forward_i))) == 0 or primes.count(list_to_int(list(backward_i))) == 0:
			truncable = 0
		forward_i.popleft()
		backward_i.pop()
	return truncable

#main
out = 0
primes = []
f = open("../../txt/primes_under_one_million.txt", "r")
for line in f:
	if line != "":
		line = int(line.strip("\n"))
		primes.append(line)
f.close()
num = 0
k = 0
while num < 11:
	if is_truncable(primes[k]) == 1:
		num += 1
		out += primes[k]
	k += 1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
