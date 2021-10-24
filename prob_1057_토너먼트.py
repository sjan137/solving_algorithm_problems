import sys

N, a, b = map(int, sys.stdin.readline().split())
vs_round = 0

while a != b:
    a -= a//2
    b -= b//2
    vs_round += 1

print(vs_round)