import time
start_time = time.time()

#returns the ith triangle number
def triangle(i):
	return i*(i+1)/2

#returns the ith pentagonal number
def pentagon(i):
	return i*(3*i-1)/2

#returns the ith hexagonal number
def hexagon(i):
	return i*(2*i-1)

#main
out = 0
triangles = []
pentagons = []
hexagons = []
for x in range(0, 100000):
	triangles.append(triangle(x))
	pentagons.append(pentagon(x))
	hexagons.append(hexagon(x))
k = 285
found = 0
while found == 0:
	k += 1
	if pentagons.count(triangles[k]) == 1:
		if hexagons.count(triangles[k]) == 1:
			found = 1
			out = triangles[k]

elapsed_time = time.time()-start_time
print "%d found in %ss" % (out, elapsed_time)
