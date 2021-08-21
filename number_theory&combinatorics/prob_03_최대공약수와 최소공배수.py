import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    div = min(n, m)
    while True:
        if m % div == 0 and n % div == 0: break
        div -= 1
    n_quot, m_quot = n//div, m//div
    print(f'{div}\n{n_quot*m_quot*div}')
    return None

if __name__ == '__main__':
    main()