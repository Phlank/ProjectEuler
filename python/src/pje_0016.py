#transforms an integer to a list of separate digits
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

out = 0
digits = int_to_list(2**1000)
for digit in digits:
	out += digit

print "%d" % (out)
