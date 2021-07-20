import sys

def hanoi(n):
    if n == 1: return 1
    else: return 2 * hanoi(n-1) + 1

def hanoiMove(n):
    if n == 1:
        return [1]
    else:
        return hanoiMove(n-1) + [n] + hanoiMove(n-1)

N = int(sys.stdin.readline())
layer_list = list(range(N, 0, -1))
print(hanoi(N))
print(hanoiMove(N))