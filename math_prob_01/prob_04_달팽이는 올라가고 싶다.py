import sys

A, B, V = map(int, sys.stdin.readline().split())
n = (V - B) / (A - B)
if n == int(n): print(int(n))
else: print(int(n) + 1)