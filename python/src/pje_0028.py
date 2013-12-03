import time
start_time = time.time()

#generates a spiral of numbers of nxn, e.g.
#7 8 9
#6 1 2
#5 4 3
#is a 3x3 number spiral
def number_spiral(n):
	if n%2 == 0: return []
	spiral = []
	for a in range(0, n):
		spiral.append([])
	for a in spiral:
		for b in range(0, n):
			a.append(0)
	center = (n-1)/2
	x, y = center, center
	last = "up"
	i = 1
	spiral[x][y] = i
	next = 0
	done = 0
	while x != n-1 or y != 0:
		if last == "up":
			if spiral[x+1][y] == 0:
				x += 1
				next = 1
			else:
				y -= 1
		elif last == "right":
			if spiral[x][y+1] == 0:
				y += 1
				next = 2
			else:
				x += 1
		elif last == "down":
			if spiral[x-1][y] == 0:
				x -= 1
				next = 3
			else:
				y += 1
		elif last == "left":
			if spiral[x][y-1] == 0:
				y -= 1
				next = 4
			else:
				x -= 1
		i += 1
		spiral[x][y] = i
		if next == 1: last = "right"
		elif next == 2: last = "down"
		elif next == 3: last = "left"
		else: last = "up"
	return spiral

#main
n = 1001
spiral = number_spiral(n)
x, y = 0, 0
out = 0
for x in range (0, n):
	out += spiral[x][x]
	y = n-x-1
	out += spiral[x][y]
out -= 1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
