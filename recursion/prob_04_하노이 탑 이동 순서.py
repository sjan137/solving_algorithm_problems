import sys

def hanoi(n):
    if n == 1: return 1
    else: return 2 * hanoi(n-1) + 1

def hanoiMove(n, start):
    if n == 1:
        return [start, 3]
    else:
        

N = int(sys.stdin.readline())
print(hanoi(N))