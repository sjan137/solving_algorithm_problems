import sys


def solve(n, num_list):
    dp = [num_list[0]] + [0] * (n-1)

    for i in range(1, n):
        dp[i] = max(dp[i-1]+num_list[i], num_list[i])
    return max(dp)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(solve(N, nums))