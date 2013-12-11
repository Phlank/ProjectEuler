n = 0
sum_of_squares = 0
square_of_sums = 0
out = 0

while n < 100:
	n = n + 1
	sum_of_squares = sum_of_squares + n ** 2
	square_of_sums = square_of_sums + n

square_of_sums = square_of_sums ** 2
out = square_of_sums - sum_of_squares

print "%d" % (out)
