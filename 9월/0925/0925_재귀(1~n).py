def f(n):
    if n<1:
        return 1
    else:
        f(n-1)
        print(n, end="\n")

n = int(input())
f(n)