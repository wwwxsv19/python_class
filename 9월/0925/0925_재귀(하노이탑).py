def f(n, a='A', b='B', c='C'):
    if n==1:
        print("Disk 1 :", a, "to", c)
    else:
        f(n-1, a, c, b)
        print("Disk", n, ":", a,"to", c)
        f(n-1, b, a, c)

n = int(input())
f(n)