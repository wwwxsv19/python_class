#이상한 출석 부르기 1
#map(int, input().split())

n = int(input())
num1 = list(map(int, input().split()))
num2 = []

for i in range(24):
    num2.append(0)

for i in range(n):
    num2[num1[i]]+=1

'''
#똑바로 출력
for i in range(1, 24):
    print(i, num2[i], end='\n')
'''

'''
#거꾸로 출력
for i in range(23, 0, -1):
    print(i, num2[i], end='\n')
'''

#python 알고리즘 : split() 활용해 리스트에 넣어서 계산
#C 알고리즘 : 