pmax = jmax = 2000

for i in range(3):
    num = int(input())
    if pmax > num:
        pmax = num

for i in range(2):
    num = int(input())
    if jmax > num:
        jmax = num

num = pmax + jmax


print(num + (num*0.1))