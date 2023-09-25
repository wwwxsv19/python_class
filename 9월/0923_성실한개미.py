num = [[0] * 12 for i in range(12)]

for i in range(10):
    n=input().split()
    for j in range(10):
        num[i+1][j+1] = int(n[j])

x = y = 2

while True :
    if num[x][y] == 0:
        num[x][y] = 9
    elif num[x][y] == 2:
        num[x][y] = 9
        break

    if (num[x][y+1]==1 and num[x+1][y]==1) or (x==9 and y==9):
        break

    if num[x][y+1] != 1:
        y += 1
    elif num[x+1][y] != 1:
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(num[i][j], end=' ')
    print()

