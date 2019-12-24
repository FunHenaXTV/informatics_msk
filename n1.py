n, x, y = map(int, input().split())

t = 0
if x > y:
	t += y
else:
	t += x

r = 10**20
l = 0

while r-l > 1:
	m = (l + r)/2
	if m/x + m/y >= n:
		r = m
	else:
		l = m

print(int(m + t))
