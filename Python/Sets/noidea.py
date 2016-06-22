input()
arr = [int(s) for s in input().split()]
s = set([int(s) for s in input().split()])
s2 = set([int(s) for s in input().split()])

h = 0

for i in arr:
    if i in s:
        h += 1
    if i in s2:
        h -= 1

print(h)