num = []

h, w = map(int, input().split())
for i in range(h):
    num.append([])
    for j in range(w):
        num[i].append(0)


n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())

    if d==0:
        for j in range(y, y+l+1):
            num[x][j]=1
    else:
        for j in range(x, x+l+1):
            num[j][y]=1


for i in range(h):
    for j in range(w):
        print(num[i][j], end=' ')
    print()