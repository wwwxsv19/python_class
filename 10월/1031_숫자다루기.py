s = input()
num = 0

for i in s: # 범위를 s로 정해 s를 하나씩 i에 대입
    num += int(i)

print(int(s[::-1]), num, sep="\n")