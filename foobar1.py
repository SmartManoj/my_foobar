#!python2
s='abcabcabcabc'

def answer(s):
	a=[s.count(s[:x]) for x in range(len(s)) if s[:x]*s.count(s[:x]) == s]
	if a:return max(a)
	return 1

print(answer('aa'))
