import itertools

def list_to_int(l):
	return int("".join(str(x) for x in l))

nums = list("0123456789")
permutations = []
for permutation in itertools.permutations(nums, 10):
	permutations.append(permutation)

out = list_to_int(permutations[999999])

print "%d" % (out)
