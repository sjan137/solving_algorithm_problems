import sys

# 파스칼의 삼각형을 통해 정확히 계산
def main():
    N, K = map(int, sys.stdin.readline().split())
    comb_arr = [[1] * (N+1) for _ in range(N+1)]

    for i in range(1, N-K+1):  # 최소한의 행까지만 계산
        for j in range(1, N+1):
            comb_arr[i][j] = comb_arr[i][j-1] + comb_arr[i-1][j]
    
    print(comb_arr[N-K][K] % 10007)
    return None

if __name__ == '__main__':
    main()