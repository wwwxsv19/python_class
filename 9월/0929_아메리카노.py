n, m = map(int, input().split())
num = cnt = 0

while(n >= m):
    num = n//m # 현재 쿠폰의 수로 먹을 수 있는 음료의 개수
    n = n - num*m # 쿠폰 얼마나 썼는지 ( 위의 음료 개수 * 정해진 쿠폰 수 )
    n = n + num # 쿠폰으로 받은 음료의 수만큼 쿠폰을 또 받음
    cnt = cnt + num # 현재 얼마나 먹었는지 더함

print(cnt)