import sys


def solve(n, dp):
    max_drink = [0] * n
    if n >= 1: max_drink[0] = dp[0]
    if n >= 2: max_drink[1] = sum(dp[:2])
    if n >= 3:
        min_in_three = dp.index(min(dp[:3]))
        max_drink[2] = sum(dp[:min_in_three]) + sum(dp[min_in_three+1:3])
    if n >= 4:
        max_drink[3] = max(dp[3]+dp[2]+dp[0], dp[3]+dp[1]+dp[0], dp[2]+dp[1])
    if n >= 5:
        for i in range(4, n):
            max_drink[i] = max(dp[i]+max(dp[i-1]+max_drink[i-3], max_drink[i-2]), dp[i-1]+dp[i-2]+max_drink[i-4])
    
    if n == 1: return max_drink[0]
    else: return max(max_drink[-1], max_drink[-2])

N = int(sys.stdin.readline())
podoju_list = [int(sys.stdin.readline()) for _ in range(N)]
print(solve(N, podoju_list))