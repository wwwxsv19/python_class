list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
n = int(input())
count = 0

for i in list:
    while i<=n:
        n -= i
        count += 1

print(count)