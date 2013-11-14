import time
start_time = time.time()

#returns the digits if i as a list
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(8)]
        while list[0] == 0:
                list.remove(0)
        return list

#main
list_of_decimals = []
x = 1
while len(list_of_decimals) < 1000000:
	for y in int_to_list(x): list_of_decimals.append(y)
	x += 1
out = list_of_decimals[0]*list_of_decimals[9]*list_of_decimals[99]*list_of_decimals[999]*list_of_decimals[9999]*list_of_decimals[99999]*list_of_decimals[999999]

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
