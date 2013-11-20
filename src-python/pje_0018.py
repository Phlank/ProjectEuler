import time
start_time = time.time()

#main
out = 0
rows = []
f = open("../txt/pje_0018_pyramid.txt", "r")
for line in f:
	line = line.split(" ")
	line = map(int, line)
	rows.append(line)
f.close()
row, col = 14, 0
while row > 0:
	row -= 1
	col = 0
	while col <= row:
		if rows[row+1][col] > rows[row+1][col+1]: rows[row][col] += rows[row+1][col]
		else: rows[row][col] += rows[row+1][col+1]
		col += 1
out = rows[0][0]

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
