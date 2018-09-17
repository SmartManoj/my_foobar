#!python2
def base(n, b):
	q,r=divmod(n,b) 
	return base(q, b)+str(r) if q else str(r)

def answer(s,b):
	a=int(s,b)
	n=[s]
	while True:
		y=''.join(sorted(s))
		x=y[::-1]
		z=base(int(x,b)-int(y,b),b).zfill(len(x))
		if z in n:return len(n)-n.index(z);break
		s=z
		n.append(z)

answer('210022',3)	
#zero



