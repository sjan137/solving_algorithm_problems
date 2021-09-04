import sys

# 동적 프로그래밍으로 풀어본 버전
def solve(n, n_list):
    dp = [1] + [0] * (n-1)
    for i in range(1, n):
        temp = 0
        for j in range(i):
            if n_list[i] > n_list[j]:
                if temp < dp[j]: temp = dp[j]
        dp[i] = temp + 1
    return max(dp)

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
print(solve(N, num_list))