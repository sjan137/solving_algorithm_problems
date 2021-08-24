import sys
from math import factorial

def main():
    N, K = map(int, sys.stdin.readline().split())
    newK = min(K, N-K)
    result = 1
    for i in range(newK):
        result = result * (N-i) / (i+1)
    print(int(result)%10007)
    return None

if __name__ == '__main__':
    main()