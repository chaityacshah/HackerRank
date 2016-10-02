#bubble sort can be optimized

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numberofSwaps = 0

for i in a:
    for j in range(n-1):
        if(a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            numberofSwaps += 1
 
print('Array is sorted in %d swaps.' % numberofSwaps)
print ('First Element:' ,a[0])
print ('Last Element:' ,a[n-1])
