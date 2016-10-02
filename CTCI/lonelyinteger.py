n = int(input())

arr = [int(x) for x in input().split()]
sum = 0
for i in arr:
    sum ^= i

print(sum)
