import time

start_time = time.time()

#returns 0 if false, 1 if true
def is_palindrome(n):
	if len(n) < 2:
		return 1
	else:
		if n[0] != n[-1]:
			return 0		
	return is_palindrome(n[1:-1])

a = 100
b = 100

a_store = a
b_store = b

product = a * b
largest_palindrome = 0

while a < 1000:
	b = 100
	while b < 1000:
		product = a * b
		product_string = str(product)
		if is_palindrome(product_string) and product > largest_palindrome:
			largest_palindrome = product
			a_store = a
			b_store = b
		b = b + 1
	a = a + 1

elapsed_time = time.time() - start_time

print "%d found in %ss" % (largest_palindrome, elapsed_time)
			
