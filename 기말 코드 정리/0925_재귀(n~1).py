'''
def f(n):
    if n < 1:
        return 1
    else:
        print(n)
        f(n-1)
'''

def f(n):
    print(n)
    if n!= 1:
        f(n-1)
        
n = int(input())
f(n)