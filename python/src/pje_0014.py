def collatz(i):
	if i == 1: return i
	elif i % 2 == 0:
		i /= 2
		return i
	else:
		i = (3*i)+1
		return i

def num_collatz_steps(i):
	steps = 0
	k = collatz(i)
	while k != 1:
		steps += 1
		k = collatz(k)
	return steps

out = 0
max = 1000000
i = 1
top_chain = 0

while i < max:
	i_steps = num_collatz_steps(i)
	if top_chain < i_steps:
		top_chain = i_steps
		out = i
	i += 1

print "%d" % (out)
