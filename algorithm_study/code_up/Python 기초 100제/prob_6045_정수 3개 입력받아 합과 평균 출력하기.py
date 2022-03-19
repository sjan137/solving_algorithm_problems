import sys

a, b, c = map(int, sys.stdin.readline().split())
n_sum = a + b + c
print(n_sum, f"{n_sum/3:.2f}")