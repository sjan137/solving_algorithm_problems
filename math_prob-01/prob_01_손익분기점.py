import sys

A, B, C = map(int, sys.stdin.readline().split())
if C <= B: print(-1)
else: print(int(A / (C - B)) + 1)