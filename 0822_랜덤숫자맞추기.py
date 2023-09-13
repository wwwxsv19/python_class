# 랜덤 숫자 맞추기
# 맞출 때까지 업 다운 알려주기
# 맞췄을 때 몇 회만에 맞췄는지 알려주기
# 예외 처리 : 문자를 입력 받았을 때 다시 시도하라고 알림

import random

rn = random.randint(1, 100)
i = 0

print("랜덤 숫자 맞추기 게임")

while True:
    num = input("정답 도전 : ")
    i += 1
    if num.isdigit() == False:
        print("정수로 다시 입력해 주세요!")
    elif rn == int(num):
        print("정답입니다!", i, "번째 만에 성공!")
        break
    else:
        print("다시 시도해 보세요!")
        if int(num) < rn:
            print("UP!")
        else:
            print("DOWN!")
