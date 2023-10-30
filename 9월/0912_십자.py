arr = []

for i in range(19):
    arr.append(list(map(int, input().split())))

num = int(input())

for i in range(num):
    x, y = map(int, input().split())
    for j in range(19):
        if arr[j-1][y-1]==0:
            arr[j-1][y-1] = 1
        else:
            arr[j-1][y-1] = 0
        
        if arr[x-1][j-1]==0:
            arr[x-1][j-1] = 1
        else:
            arr[x-1][j-1] = 0

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=" ")
    print()