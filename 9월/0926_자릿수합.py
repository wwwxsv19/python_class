n = int(input())
num = 0

while num == 0 or num > 9: # 왜 num 조건이 이런가?
    num = 0
    while(n>0):
        num += int(n%10)
        n = int(n/10)
    n = num

print(num)

'''
while 문의 num 조건이 저런 이유 :
    num 은 n 의 자릿수라고 생각하면 된다
    초기화를 위해 0 허용, 애초에 자릿수가 0인 수는 없음
    자릿수가 1이면 더이상 계산할 필요가 없으므로
    한 자릿수 중 가장 큰 9로 조건 설정
'''