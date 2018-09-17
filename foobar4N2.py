#!python2
slopes={}
maps=[]
def gcd(a,b):
	if b==0:
		return abs(a)
	else:
		return abs(gcd(b,a%b))
def answer(dim,cp,bp,dist1):
	global slopes,maps,x,y,bx,by,dist,rm,lm,tm,bm
	
	dist=dist1
	captured={}
	vectors={}
	wExtend=1+(dist+cp[0])/dim[0]
	hExtend=1+(dist+cp[1])/dim[1]
	x=cp[0]
	y=cp[1]
	bx=bp[0]
	by=bp[1]
	delY=by-y
	delX=bx-x
	delGCD=gcd(delX,delY)
	delD=(delY**2+delX**2)**.5
	delY/=delGCD
	delX/=delGCD
	
	cnt=0
	if(dist - delD >=0):
		cnt=1
		captured[(bx,by)]=1
		slopes[(delY,delX)]=delGCD		
		vectors[(delY,delX)]=1
	fillH(x,y,hExtend,dim,True)
	fillV(x,y,hExtend,wExtend,dim,True)
	fillH(bp[0],bp[1],hExtend,dim,False)
	fillV(bp[0],bp[1],hExtend,wExtend,dim,False)
	for i in range(len(maps)):
		m=maps[i]
		if captured.get((m[0],m[1]))==None:
			delY=m[1]-y
			delX=m[0]-x
			delGCD=gcd(delX,delY)
			delX/=delGCD
			delY/=delGCD
			sm=slopes.get((delY,delX))
			if vectors.get((delY,delX)) ==None:
				print cnt,delY,delX,sm
				if sm==None:
					cnt+=1
					vectors[(delY,delX)]=1
				else:
					if delGCD<sm:
						cnt+=1
						vectors[(delY,delX)]=1

			captured[(m[0],m[1])]=1
	slopes.clear()
	maps[:]=[]
	captured.clear()
	vectors.clear()
	return cnt

def a2map(cx,cy):
	global slopes,maps,x,y,bx,by,dist,rm,lm,tm,bm
	delY=cy-y
	delX=cx-x
	tget=[cx,cy]
	delD=(delY**2+delX**2)**.5
	if dist-delD>=0:
		maps.append(tget)

def addSlope(cx,cy):
	global slopes,maps,x,y,bx,by,dist,rm,lm,tm,bm
	delY=cy-y
	delX=cx-x
	delGCD=gcd(delX,delY)
	delD=(delY**2+delX**2)**.5
	delX/=delGCD
	delY/=delGCD
	if dist-delD>=0:
		if slopes.get((delY,delX))==None:
			slopes[(delY,delX)]=delGCD
		elif delGCD<slopes.get((delY,delX)):
			slopes[(delY,delX)]=delGCD

def fillV(cx1,cy,hExtend,wExtend,dim,isH):
	global slopes,maps,x,y,bx,by,dist,rm,lm,tm,bm
	if isH:
		rm=dim[0]-x
		lm=x
	else:
		rm=dim[0]-bx
		lm=bx

	cx=cx1
	for i in range(wExtend):
		cx+=rm*2
		rm=dim[0]-rm
		if isH:
			addSlope(cx,cy)
		else:
			a2map(cx,cy)
		fillH(cx,cy,hExtend,dim,isH)
	cx=cx1
	for i in range(wExtend):
		cx-=lm*2
		lm=dim[0]-lm
		if isH:
			addSlope(cx,cy)
		else:
			a2map(cx,cy)
		fillH(cx,cy,hExtend,dim,isH)


def fillH(cx,cy1,hExtend,dim,isH):
	global slopes,maps,x,y,bx,by,dist,rm,lm,tm,bm
	if isH:
		tm=dim[1]-y
		bm=y
	else:
		tm=dim[1]-by
		bm=by

	cy=cy1
	for i in range(hExtend):
		cy+=tm*2
		tm=dim[1]-tm
		if isH:
			addSlope(cx,cy)
		else:
			a2map(cx,cy)

	cy=cy1
	for i in range(hExtend):
		cy-=bm*2
		bm=dim[1]-bm
		if isH:
			addSlope(cx,cy)
		else:
			a2map(cx,cy)

# print(answer([3, 2],[1, 1],[2, 1],4))

# print(answer([300, 275],[150, 150],[185, 100],500))