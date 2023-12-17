def f(n, num, t=0):
    if t == n:
        return
    for i in range(t, n+t):
        print(num[i%n], end=' ')
    print()
    f(n, num, t + 1)

n = int(input())
num = list(map(int, input().split()))

f(n, num)
