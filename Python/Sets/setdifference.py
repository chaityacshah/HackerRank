a=int(input())
s = set(map(int, input().split())) 

b=int(input())
s2 = set(map(int, input().split())) 

print(len(s.difference(s2)))