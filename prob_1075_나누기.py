import sys

N = int(sys.stdin.readline().strip()[:-2] + '00')
F = int(sys.stdin.readline())

while N % F:
    N += 1

print(str(N)[-2:])