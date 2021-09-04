import sys

# Knapsack 알고리즘(0-1 Knapsack)
def solve(n, k, wv_list):
    dp = [[0] * (k+1) for _ in range(n+1)]
    new_wv_list = [[0, 0]] + wv_list

    for i in range(1, n+1):
        for j in range(1, k+1):
            now_w, now_v = new_wv_list[i]
            if now_w <= j: dp[i][j] = max(dp[i-1][j], now_v + dp[i-1][j-now_w])
            else: dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

N, K = map(int, sys.stdin.readline().split())
WV = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solve(N, K, WV))