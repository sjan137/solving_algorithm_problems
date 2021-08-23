import sys


def gcd(a, b):
    return gcd(b%a, a) if b%a else a

def main():
    N = int(sys.stdin.readline())
    radius = list(map(int, sys.stdin.readline().split()))

    for i in range(1, N):
        gcd_num = gcd(radius[0], radius[i])
        print(f'{radius[0]//gcd_num}/{radius[i]//gcd_num}')

    return None

if __name__ == '__main__':
    main()