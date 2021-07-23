import sys

def hanoi(n):
    if n == 1: return 1
    else: return 2 * hanoi(n-1) + 1

def hanoiMove(n, st1, st2, st3):
    if n == 1: print(st1, st3)
    else:
        hanoiMove(n-1, st1, st3, st2)
        print(st1, st3)
        hanoiMove(n-1, st2, st1, st3)

N = int(sys.stdin.readline())
print(hanoi(N))
hanoiMove(N, 1, 2, 3)