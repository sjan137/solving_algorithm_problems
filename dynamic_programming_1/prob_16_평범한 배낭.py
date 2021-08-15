import sys

# Knapsack 알고리즘(0-1 Knapsack)
def solve(n, k, wv_list):
    dp = [[0] * k for _ in range(n)]

    for i in range(k):
        for j in range(n):
            now_w, now_v = wv_list[j]
            if now_w <= i+1: dp[j][i] = max(dp[j-1][i], now_v + dp[j-1][i-now_w])
            else: dp[j][i] = dp[j-1][i]

    return dp

N, K = map(int, sys.stdin.readline().split())
WV = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solve(N, K, WV))