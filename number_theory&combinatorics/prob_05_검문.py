import sys


def gcd(a, b):
    return gcd(b%a, a) if b%a else a

def solve(n, n_list):
    gcd_list = []
    n_list.sort()
    
    # 정렬된 리스트의 숫자에서 각각 차이를 구하고, 그 차이들의 최대공약수를 저장
    if n == 2: gcd_list.append(n_list[1]-n_list[0])
    else:
        for i in range(1, n-1):
            temp = gcd(n_list[i+1]-n_list[i], n_list[i]-n_list[i-1])
            if temp not in gcd_list: gcd_list.append(temp)

    # 최대공약수 사이의 최대공약수를 구해서 가장 공통적인 최대공약수 구하기
    gcd_num = gcd_list[0]
    for i in range(1, len(gcd_list)):
        gcd_num = gcd(gcd_num, gcd_list[i])

    # result = [gcd_num]
    # for i in range(2, int(gcd_num**0.5)+1):
    #     if gcd_num % i == 0: 
    #         result.append(i)
    #         result.append(gcd_num//i)
    # result = list(set(result))
    # print(*result)
    result = []
    for i in range(2, gcd_num+1):
        if gcd_num % i == 0: result.append(i)
    print(*result)
    return None

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
solve(N, numbers)