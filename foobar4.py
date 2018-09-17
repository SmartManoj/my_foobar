#!python2
from itertools import combinations
def answer(nb, nr):
	keys = [[] for i in xrange(nb)]
	cnt = nb - (nr - 1)
	for index, item in enumerate(combinations(xrange(nb), cnt)):
		for i in item:
			keys[i].append(index)
	return keys
