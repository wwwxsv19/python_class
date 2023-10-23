# 문자열을 받아 서브스트링 ( 특정 위치부터 몇 글자 추출 )

num = input()
x, y = map(int, input().split())

print(num[x: x+y])