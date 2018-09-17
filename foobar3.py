#!python2
def xor(a,b):
	return f(b)^f(a-1)
def f(a):
	return [a,1,a+1,0][a%4]
def answer(s,l):
	c=s
	z=0
	for i in xrange(l):
		z^=xor(s+l*i,s+(l-1)*(i+1))		
	return z

print(answer(17,4))
