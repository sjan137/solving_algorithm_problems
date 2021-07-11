N = int(input())
n = 2
result = list()
while N != 1:
    if N % n == 0:
        result.append(n)
        N = N // n
    else: n += 1

for i in result:
    print(i)