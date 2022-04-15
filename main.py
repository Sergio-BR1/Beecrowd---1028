def mdc(y, r):
    if y%r == 0:
        return r
    return(mdc(r, y%r))
    
casos = int(input())

for i in range (casos):
	a, b = map(int, input().split())
	c = min(a,b)
	d = max(a,b)
	if d%c == 0:
		print(c)
	else:
		print(mdc(c,d%c))