N = int(input())
count = 0
if N % 5 == 0:
    print(N // 5)
elif N % 3 == 0:
    print(N // 3)
else:
    while True:
        N -= 5
        count += 1
        if N % 3 == 0:
            print(N // 3 + count)
            break
        if N < 3:
            print(-1)
            break