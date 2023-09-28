n = int(input())
num = list(map(int, input().split()))

sorted_num = sorted(num, reverse=True)

print(sorted_num)

for i in range(n):
    sc = sorted_num.index(num[i]) + 1
    print(num[i], sc)