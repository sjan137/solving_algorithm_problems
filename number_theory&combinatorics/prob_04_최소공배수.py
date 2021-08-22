import sys


def main():
    def gcd(a, b):
        return gcd(b%a, a) if b%a else a
    
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = list(map(int, sys.stdin.readline().split()))
        gcd_num = gcd(a, b)
        print((a * b) // gcd_num)
    return None

if __name__ == '__main__':
    main()