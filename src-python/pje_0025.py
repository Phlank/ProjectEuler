import time
start_time = time.time()

#main
f_nums = [1, 1]
t = 1
while len(str(f_nums[t])) < 1000:
	t += 1
	f_nums.append(f_nums[t-1]+f_nums[t-2])

out = t+1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
