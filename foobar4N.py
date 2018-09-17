#!python2 
import sys
mset=set()
perm=[]
def permute(ss,at,index):
	global mset,perm
	s=ss[index]
	for i in range(at,len(s)):
		s[i],s[at]=s[at],s[i]
		if not mset.issuperset(s):
			mset.add(tuple(s))
			perm.append(s)
		permute(ss,at+1,index)
		s[i],s[at]=s[at],s[i]

def mcmp(a,b):
	if len(a)!=len(b):
		return len(b)-len(a)
	else:
		for i in range(len(a)):
			z=a[i]-b[i]
			if z:return z
	return 1

def subsets(b):
	maxi=2**b-1
	maxl=len(bin(maxi))-2
	ss=[]
	while maxi>=0:
		bb=bin(maxi)[2:].zfill(maxl)
		s=[]
		for i in range(len(bb)):
			if bb[i]=='1':
				s.append(i)
		ss.append(s)
		maxi-=1
	sss=sorted(ss,mcmp)
	return sss
def answer(t, tl):
	try:
			
		global perm
		l=len(t)
		ss=subsets(l-2)
		mini=[[None] * l for _ in range(l)]
		for z in range(l):
			for s in range(l):
				if z==0:
					for i in range(l):
						mini[s][i]=sys.maxsize
					mini[s][s]=0;
				for i in range(l):
					for j in range(l):
						if mini[s][i] != sys.maxsize and mini[s][i]+ t[i][j] < mini[s][j]:
							mini[s][j] = mini[s][i] + t[i][j]


		for s in range(l):
			for i in range(l):
				for j in range(l):
					if mini[s][i]+t[i][j]<mini[s][j]:
						cc=[0]*(l-2)
						for c in range(l-2):
							cc[c]=c
						return cc

		for ix in range(len(ss)):
			permute(ss,0,ix)
			for p in range(len(perm)):
				f=0
				z=tl
				pp=perm[p]
				for i in range(len(pp)):
					z-=mini[f][pp[i]+1];
					f=pp[i]+1

				z-=mini[f][l-1]
				if z>=0:
					rr=[0]*len(ss[ix])
					for r in range(len(ss[ix])):
						rr[r]=ss[ix][r]
					return rr


	except:pass




print(answer([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]],1)	)

