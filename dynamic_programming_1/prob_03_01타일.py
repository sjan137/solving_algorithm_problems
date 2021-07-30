import sys

# 결과는 피보나치 수열을 따름.
def binaryTile(n):
    if n == 1: return result[0]
    elif n == 2: return result[1]
    else:
        for i in range(2, n):
            if not result[i]:
                result[i] = result[i-2] + result[i-1]
        return result[n-1]

N = int(sys.stdin.readline())
result = [1, 2] + [0] * (N - 2)
print(binaryTile(N))