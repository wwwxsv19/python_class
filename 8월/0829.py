# 좌표 입력 받아 해당 좌표는 1로 바꾸기

p = []
for i in range(20):
    p.append([])
    for j in range(20):
        p[i].append(0)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    p[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(p[i][j], end=' ')
    print()

