import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
n = (V - B) / (A - B)
print(math.ceil(n))