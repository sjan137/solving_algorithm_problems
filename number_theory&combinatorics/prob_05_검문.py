import sys

def gcd(a, b):
    return gcd(b%a, a) if b%a else a

def getDiv(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i: continue
        result.append(i)
        if n // i != i: result.append(int(n//i))
    return sorted(result[1:])

def solve(n, n_list):
    # 정렬된 리스트의 숫자에서 각각 차이를 구하고, 그 차이들의 최대공약수를 저장
    n_list.sort()
    diff_list = list(set([n_list[i]-n_list[i-1] for i in range(1, n)]))
    gcd_num = diff_list[0]
    for i in range(1, len(diff_list)):
        gcd_num = min(gcd_num, gcd(diff_list[i], diff_list[i-1]))
    return getDiv(gcd_num)

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
print(*solve(N, numbers))