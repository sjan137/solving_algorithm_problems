import sys


def solve(n, k, coins):
    count = 0
    for i in range(n):
        if coins[-(i+1)] > k or k == 0: continue
        temp_count, k = divmod(k, coins[-(i+1)])
        count += temp_count

    return count

N, K = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for _ in range(N)]
print(solve(N, K, coin_list))