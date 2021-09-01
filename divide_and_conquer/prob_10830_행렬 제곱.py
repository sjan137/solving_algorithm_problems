import sys

# b == 1일 때, a 반환
# b가 홀수일 때, dotAB(dotAA(getPowerMatrix(a, b//2, n), n), a, n)
# b가 짝수일 때, dotAA(getPowerMatrix(a, b//2, n), n)
def getPowerMatrix(a, b, n):
    if b == 1: return a
    elif b % 2: return dotAB(dotAA(getPowerMatrix(a, b//2, n), n), a, n)
    else: return dotAA(getPowerMatrix(a, b//2, n), n)

# 한 행렬의 제곱을 계산
def dotAA(a, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * a[k][j]
            result[i][j] %= 1000
    return result

# 두 행렬의 곱셈 계산
def dotAB(a, b, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

def main():
    N, B = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    result = getPowerMatrix(A, B, N)

    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000
    
    return result

if __name__ == "__main__":
    for row in main():
        print(' '.join(map(str, row)))