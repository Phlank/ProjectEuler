#transforms an integer into a list
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

out = 0
i = 2
max = 6*9**5
while i < max:
	i_list_sum = 0
	i_list = int_to_list(i)
	for x in i_list:
		i_list_sum += x**5
	if i == i_list_sum:
		out += i
	i += 1

print "%d" % (out)
