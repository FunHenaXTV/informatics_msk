n, x, y = map(int, input().split())

t = 0
if x > y:
	t += y
else:
	t += x

r = 10**32
l = 0
n -= 1

while r-l > 1:
	m = (l + r)//2
	if m/x + m/y >= n:
		r = m
	else:
		l = m
print(r+t)
