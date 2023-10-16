# 리스트 값을 전부 더해서 출력, 단 재귀로 풀 것

def f(arr):
    if not arr:
        return 0
    else:
        return arr.pop() + f(arr)

list = list(map(int, input().split()))

print(f(list))