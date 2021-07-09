N = int(input())
count = list()
a5 = N // 5
for i in range(0, a5 + 1):
    b3 = (N - 5 * i) % 3
    if b3 == 0:
        a3 = (N - 5 * i) // 3
        count.append(i + a3)
if len(count) == 0: print(-1)
else: print(min(count))