import time
start_time = time.time()

#returns i as a list
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

#returns l as an int
def list_to_int(l):
        return int("".join(str(x) for x in l))

#main
out = 0
mults = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in range(1, 10000):
	possible_pandigital = []
	i = 0
	while len(possible_pandigital) < 9:
		temp_list = int_to_list(n*mults[i])
		for x in temp_list: possible_pandigital.append(x)
		i += 1
	is_pandigital = 0
	if len(possible_pandigital) == 9:
		is_pandigital = 1
		for x in possible_pandigital:
			if possible_pandigital.count(x) != 1 or possible_pandigital.count(0) != 0: is_pandigital = 0
	if is_pandigital == 1:
		if out < list_to_int(possible_pandigital): out = list_to_int(possible_pandigital)

elapsed_time = time.time()-start_time
print "%d found in %ss" % (out, elapsed_time)
