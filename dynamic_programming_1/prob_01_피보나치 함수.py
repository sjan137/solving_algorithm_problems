import sys

def fibonacci(n):
    global count_0
    global count_1
    for _ in range(n):
        count_0, count_1 = count_1, (count_0+count_1)
    print(count_0, count_1)

N = int(sys.stdin.readline())
for _ in range(N):
    count_0 = 1
    count_1 = 0
    fibonacci(int(sys.stdin.readline()))