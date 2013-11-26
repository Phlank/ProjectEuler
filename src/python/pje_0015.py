import time
start_time = time.time()

import math

#returns pascal's triangle of height h
def pascal(h):
	triangle = [[1]]
	current_level = 1
	while current_level < h:
		new_level = []
		i = 0
		while i <= current_level:
			if i == 0 or i == current_level: new_level.append(1)
			else: new_level.append(triangle[current_level-1][i-1]+triangle[current_level-1][i])
			i += 1
		triangle.append(new_level)
		current_level += 1
	return triangle

#main
out = pascal(41)[40][20]

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
