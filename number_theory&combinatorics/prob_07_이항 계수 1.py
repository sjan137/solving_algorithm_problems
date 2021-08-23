import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    new_K = min(K, N-K)
    result = 1
    for i in range(new_K):
        result = result * (N-i) / (i+1)
    print(int(result))
    return None

if __name__ == "__main__":
    main()