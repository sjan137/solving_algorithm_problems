import sys


def solve(n):
    count = [0] * n
    if n >= 2: count[1] = 1
    if n >= 3: count[2] = 1
    for i in range(4, n+1):
        count[i-1] = 1 + min(count[i//2-1]+i%2, count[i//3-1]+i%3)
    return count[-1]

N = int(sys.stdin.readline())
print(solve(N))