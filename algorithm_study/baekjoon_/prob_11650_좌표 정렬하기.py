import sys

N = int(sys.stdin.readline())
locations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for xy in sorted(locations):
    print(*xy)