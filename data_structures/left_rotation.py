n, r = input().strip().split(' ')
a = list(map(int, input().strip().split(' ')))
n = int(n)
r = int(r)
for i in range(n-r):
	print(a[i+r], end = ' ')
for i in range(r):
	print(a[i], end = ' ')
