import sys

def check(s, e):
    n = e - s + 1
    for i in range(2, int(e**0.5)+1):
        for j in range(s, e+1):
            if j % (i**2) == 0:
                n -= 1
                continue
    return n

start, end = map(int, sys.stdin.readline().split())
print(check(start, end))