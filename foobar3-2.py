#!python2
def answer(M,F):
	M,F=int(M),int(F)
	c1=0
	z=-1
	while M>0 and F>0:
		if M==1:c1+=F-M;z=0;break
		if F==1:c1+=M-F;z=0;break
		if M>F:x,M=divmod(M,F)
		else:x,F=divmod(F,M)
		c1+=x
	if z==-1:z='impossible'
	else:z=c1
	return z

print(answer(2,4))
