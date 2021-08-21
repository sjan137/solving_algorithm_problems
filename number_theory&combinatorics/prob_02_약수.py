import sys


def main():
    N = int(sys.stdin.readline())
    divisor = list(map(int, sys.stdin.readline().split()))
    print(max(divisor) * min(divisor))
    return None

if __name__ == '__main__':
    main()