import sys


def solve(n):
    count = [0] * n
    if n >= 2: count[1] = 1
    if n >= 3: count[2] = 1
    i = 0
    while count.count(0) != 1:
        i += 1
        for j in range(1, n+1):
            if count[j-1] != i: continue
            else:
                for k in [j+1, j*2, j*3]:
                    if k > n: continue
                    if not count[k-1]: count[k-1] = i+1
    return count[-1]

N = int(sys.stdin.readline())
print(solve(N))