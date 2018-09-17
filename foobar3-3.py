#!python2
def answer(l):
	ll=len(l)
	c=0
	pc = [0] * len(l)
	for z in xrange(2,ll):
		for y in xrange(1,z):
			if l[z]%l[y]:continue
			pc[y]+=1
	for y in xrange(1,ll-1):
		for x in xrange(y):
			if l[y]%l[x]:continue
			c+=pc[y]
	return c

z=[1, 2, 3, 4, 5, 6]
print(answer(z))
