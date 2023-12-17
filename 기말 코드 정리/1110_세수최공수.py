def f(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b, c = map(int, input().split())

num = f(a, b)
num = f(num, c)

print(num)
