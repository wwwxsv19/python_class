s = list(map(int, input().split()))
s.sort() # 정렬하는 함수 씀
for i in range(3):
    print(s[i], end=" ")