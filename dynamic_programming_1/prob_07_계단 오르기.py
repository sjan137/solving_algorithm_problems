import sys

# 각 계단 위치에 따라 내가 얻을 수 있는 최대값을 차근차근 구해가기
def step_stairs(n, stairs_score):
    dp = [0] * n
    dp[0] = stairs_score[0]
    if n >= 2: dp[1] = dp[0] + stairs_score[1]
    if n >= 3: dp[2] = max(dp[0], stairs_score[1]) + stairs_score[2]
    if n >= 4:
        for i in range(3, n):
            dp[i] = stairs_score[i] + max(dp[i-2], dp[i-3] + stairs_score[i-1])
    print(dp[n-1])

N = int(sys.stdin.readline())
stairs_score = [int(sys.stdin.readline()) for _ in range(N)]
step_stairs(N, stairs_score)