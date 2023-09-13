num = []

for i in range(19):
    num.append(list(map(int, input().split())))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if num[j-1][y-1] == 1:
            num[j-1][y-1] = 0
        else:
            num[j-1][y-1] = 1
    for j in range(19):
        if num[x-1][j-1] == 1:
            num[x-1][j-1] = 0
        else:
            num[x-1][j-1] = 1

for i in range(19):
    for j in range(19):
        print(num[i][j], end=' ')
    print()