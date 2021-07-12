import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    isPrime = [False] * 2 + [True] * (2*n-1)
    for i in range(2, int((2*n)**0.5)+1):
        if isPrime[i]:
            for j in range(2*i, 2*n+1, i):
                isPrime[j] = False
    print(isPrime[n+1:].count(True))