import sys

def binaryTile(n):
    if n < 3: return n
    else:
        first, second = 1, 2
        for _ in range(n-2):
            first, second = second, (first + second) % 15746
        return second

N = int(sys.stdin.readline())
print(binaryTile(N))