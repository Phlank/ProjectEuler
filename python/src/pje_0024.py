import time
start_time = time.time()

import itertools

def list_to_int(l):
	return int("".join(str(x) for x in l))

#main
nums = list("0123456789")
permutations = []
for permutation in itertools.permutations(nums, 10):
	permutations.append(permutation)

out = list_to_int(permutations[999999])

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
