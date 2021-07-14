import sys


def getFactorial(n):
    if n <= 1: return 1
    else: return n * getFactorial(n-1)

N = int(sys.stdin.readline())
print(getFactorial(N))