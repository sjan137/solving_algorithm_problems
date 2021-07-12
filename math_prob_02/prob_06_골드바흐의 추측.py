import sys


def goldbachPartition(n, isPrime):
    n_half = n // 2
    if (n_half > 2) & (n_half % 2 == 0):
        goldbach_1 = n_half - 1
        goldbach_2 = n_half + 1
    else:
        goldbach_1 = n_half
        goldbach_2 = n_half
    while isPrime[goldbach_2] * isPrime[goldbach_1] != 1:
        goldbach_1 -= 2
        goldbach_2 += 2
    print(goldbach_1, goldbach_2)

T = int(sys.stdin.readline())
n_list = [0] * T
for t in range(T):
    n_list[t] = int(sys.stdin.readline())
n_max = max(n_list)
isPrime = [False] * 2 + [True] * (n_max-1)
for i in range(2, int(n_max**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, n_max+1, i):
            isPrime[j] = False
for n in n_list:
    goldbachPartition(n, isPrime)