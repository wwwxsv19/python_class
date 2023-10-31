s = (input())
num = str(int(s)+int(s[::-1])) 
# 문자열을 정수형으로 변환, 더한 후 다시 문자열로

if num == num[::-1]:
    print("YES")
else:
    print("NO")