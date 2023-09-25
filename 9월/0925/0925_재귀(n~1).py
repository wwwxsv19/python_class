def f(n):
    if n<1:
        return 1
    else:
        print(n, end="\n")
        f(n-1)

n = int(input())
f(n)