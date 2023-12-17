n = int(input())
num = list(map(int, input().split()))

sorted_num = sorted(num, reverse=True)

print(sorted_num)

for i in range(n):
    sc = sorted_num.index(num[i]) + 1 # 찾는 값이 그 배열의 몇 번째 인덱스에 있는가? 를 저장
    print(num[i], sc)