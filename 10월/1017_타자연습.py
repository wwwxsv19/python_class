# 타자 프로그램 만들기
# 문자열이 랜덤으로 주어지면 타자를 입력해서 정확도와 속도를 알려주는 프로그램을 만들어 보자

import random
import time

lst=[
    "안녕하세요 제 이름은 박강은 편안할 강에 온화할 은",
    "가은 아니고 강은 강인 아니고 강은",
    "제발 제 이름 기억해주세요 제발요",
    "감사합니다 제 이름은 강은이에요"
]

random.shuffle(lst) # lst 의 원소들을 셔플

for i in lst: # i 안에 lst 의 원소들이 차례차례 들어옴
    start = time.time()
    userIn = str(input(i+'\n')).strip() # user 가 보고 입력할 문장이 출력된 후, 그 아래에 입력을 받기 위해 줄바꿈
    end = time.time() - start # 입력이 끝난 후 찍은 시간 - 처음 시작할 때 시간

    crt = 0
    for index, c in enumerate(userIn): # index c 에 각각 userIn 의 인덱스 번호와 그 해당 값
        if index >= len(i):
            break
        if c==i[index]:
            crt+=1

    total = len(i)

    c = crt / total * 100
    e = (total - crt) / total * 100
    speed = crt / end * 60

    print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 : {:0.2f}".format(speed, c, e))