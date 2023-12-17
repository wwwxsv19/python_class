'''
a, b = map(int, input().split())

while a%b != 0:
    a, b = b, a%b

print(b)
'''

'''
def f(a, b):
    if a%b == 0:
        return b
    return f(b, a%b)

a, b = map(int, input().split())
print(f(a, b))
'''

'''
def f(a, b):
    if b == 0:
        return a
    return f(b, a%b)

a, b = map(int, input().split())
print(f(a, b))
'''