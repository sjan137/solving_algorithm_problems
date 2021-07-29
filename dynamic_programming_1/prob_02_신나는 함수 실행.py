import sys

def originW(a, b, c):
    if a <= 0 or b <= 0 or c<= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return originW(20, 20, 20)

    elif a < b and b < c:
        return originW(a, b, c-1) + originW(a, b-1, c-1) - originW(a, b-1, c)
    
    else:
        return originW(a-1, b, c) + originW(a-1, b-1, c) + originW(a-1, b, c-1) - originW(a-1, b-1, c-1)

def recursionW(a, b, c):
    return a+b+c

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1: break
    print(originW(a, b, c))