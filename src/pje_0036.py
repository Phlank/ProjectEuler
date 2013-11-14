import time
start_time = time.time()

#returns a list of digits of i
def int_to_list(i):
        list = [int(x) for x in str(i).zfill(1000)]
        while list[0] == 0:
                list.remove(0)
        return list

#reverses a list
def reverse(l):
	reverse_list = []
	x = len(l)-1
	while x >= 0:
		reverse_list.append(l[x])
		x -= 1
	return reverse_list

#returns an int from the digits in l
def list_to_int(l):
        return int("".join(str(x) for x in l))

#returns 1 if i is palindromic and 0 otherwise
def is_palindrome(i):
	i_list = int_to_list(i)
	if i_list == reverse(i_list):
		return 1
	else:
		return 0

#returns i as a binary number
binary_list = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
binary_list_length = len(binary_list)
def to_binary(i):
	i_binary_list = []
	i_started = 0
	for x in range(0, binary_list_length):
		if i >= binary_list[x]:
			i_binary_list.append(1)
			i -= binary_list[x]
			if i_started == 0: i_started = 1
		elif i_started == 1:
			i_binary_list.append(0)
	i_binary = list_to_int(i_binary_list)
	return i_binary

#main
out = 0
n = 1
while n < 1000000:
	if is_palindrome(n) == 1:
		if is_palindrome(to_binary(n)) == 1:
			out += n
	n += 2

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
