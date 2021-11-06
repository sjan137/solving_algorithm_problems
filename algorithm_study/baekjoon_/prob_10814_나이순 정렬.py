import sys

N = int(sys.stdin.readline())
names = [sys.stdin.readline().split() for _ in range(N)]

for row in sorted(names, key=lambda x: int(x[0])):
    print(*row)