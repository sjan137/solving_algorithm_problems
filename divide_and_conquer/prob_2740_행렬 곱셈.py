import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    arrA = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    M, K = map(int, sys.stdin.readline().split())
    arrB = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    result = [[0] * K for _ in range(N)]

    for i in range(N):
        for j in range(K):
            for k in range(M):
                result[i][j] += arrA[i][k] * arrB[k][j]
    return result

if __name__ == "__main__":
    for row in main():
        print(' '.join(map(str, row)))