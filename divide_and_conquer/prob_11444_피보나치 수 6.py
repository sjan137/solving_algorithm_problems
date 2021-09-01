import sys

# 행렬의 곱으로 피보나치 수열 연산 가능
# [[Fn+1, Fn], [Fn, Fn-1]] = [[1, 1], [1, 0]] ^ n
def dotAB(a, b):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

def getFibonacci(arr, n):
    if n == 1: return arr
    fibo = getFibonacci(arr, n//2)
    if n % 2: return dotAB(arr, dotAB(fibo, fibo))
    else: return dotAB(fibo, fibo)

def main():
    n = int(sys.stdin.readline())
    fibo_arr = [[1, 1], [1, 0]]
    Fn = getFibonacci(fibo_arr, n)[0][1]
    return Fn % 1000000007

if __name__ == "__main__":
    print(main())