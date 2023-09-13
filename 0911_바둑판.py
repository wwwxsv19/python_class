n = int(input())
num = []

for i in range(19):
    num.append([])
    for j in range(19):
        num[i].append(0)

for i in range(n):
    x, y = map(int, input().split())
    num[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(num[i][j], end=' ')
    print()

