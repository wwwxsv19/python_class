def f(n):
    if n==0:
        return 0
    else:
        return n+f(n-1)

n = int(input())
num = f(n)

for i in range(1, n+1):
    for j in range(0, i):
        print(num, end=' ')
        num -= 1
    print()