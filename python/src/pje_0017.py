out = 0
f = open("../../txt/pje_0017_nums.txt", "r")
for line in f:
	out += len(line.strip("\n"))

print "%d" % (out)
