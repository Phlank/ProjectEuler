import time
start_time = time.time()

out = 0

#establishes the grid from the text file
grid = []
f = open("../txt/pje_0011_grid.txt", "r")
for line in f:
	temp = line.strip("\n")
	temp = temp.split(" ")
	temp = map(int, temp)
	grid.append(temp)
f.close()

#horizontal
i, j = 0, 0
while i < 19:
	j = 0
	while j < 17:
		product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
		if out < product: out = product
		j = j + 1
	i = i + 1

#vertical
i, j = 0, 0
while j < 19:
	i = 0
	while i < 17:
		product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
		if out < product: out = product
		i = i + 1
	j = j + 1

#ul-dr diagonal
i, j = 0, 0
while i < 17:
	j = 0
	while j < 17:
		product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
		if out < product: out = product
		j = j + 1
	i = i + 1

#dl-ur diagonal
i, j = 0, 0
while i < 17:
	j = 0
	while j < 17:
		product = grid[i+3][j] * grid[i+2][j+1] * grid[i+1][j+2] * grid[i][j+3]
		if out < product: out = product
		j = j + 1
	i = i + 1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
