import sys

def fibonacci(n):
    global count_0
    global count_1

    if n == 0:
        count_0 += 1
        return

    elif n == 1:
        count_1 += 1
        return

    else:
        fibonacci(n-1)
        fibonacci(n-2)
        return

N = int(sys.stdin.readline())
for _ in range(N):
    count_0 = 0
    count_1 = 0
    fibonacci(int(sys.stdin.readline()))
    print(count_0, count_1)