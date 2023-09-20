n = int(input())
num = [int(input()) for _ in range(n)] 

def jump(n, i=2):
    p[i] = max(p[i-3]+num[i-1]+num[i], p[i-2]+num[i])
    if n <= i:
        print(p[-1])
    else:
        jump(n, i+1)

p=[0]*(n)

if len(num)<=2:
    print(sum(num))
else: 
    p[0] = num[0]
    p[1] = num[0]+num[1]
    jump(n-1)