#!python2
def answer(tl):
	a=b=1	
	s=c1=2 if tl>=10 else 0
	c2=0
	print(s,c1)
	while True:
		a,b=a+b,a
		s+=a
		if s>tl:break
		c1+=1
	for i in xrange(1,tl+1):
		_=2**(i-1)-1+2**(i-2)+2**(i-3)
		if _>tl:
			c2=i-1
			break
	return (c1-c2)

print(answer(10))
