import sys


def main():
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a == b == 0: break
        if a % b == 0: print('multiple')
        elif b % a == 0: print('factor')
        else: print('neither')
    return None

if __name__ == '__main__':
    main()