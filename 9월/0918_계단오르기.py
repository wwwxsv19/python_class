n = int(input())
num = [int(input()) for _ in range(n)] 

jump=[0]*(n) 
if n<=2:
    print(sum(num))
else: 
    jump[0] = num[0]
    jump[1] = num[0]+num[1]
    for i in range(2,n):
        jump[i] = max(jump[i-3]+num[i-1]+num[i], jump[i-2]+num[i])
        print(jump[-1])