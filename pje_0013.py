import time
start_time = time.time()

def int_to_list(i):
	list = [int(x) for x in str(i).zfill(1000)]
	while list[0] == 0:
		list.remove(0)
	return list

def list_to_int(l):
	return int("".join(str(x) for x in l))

out = 0
sum = 0
nums = []
f = open("pje_0013_nums.txt", "r")
for line in f:
	nums.append(line)
f.close()
nums = map(int, nums)
i = 0
while i < len(nums):
	sum += nums[i]
	i += 1
sum_array = int_to_list(sum)
out_array = sum_array[0:10]
out = list_to_int(out_array)

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
