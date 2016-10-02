n = int(input())
n = n-1
def fib(n):
    if(n<3):
        return n
    return fib(n-1) + fib(n-2)

ans = fib(n)
print(ans)
