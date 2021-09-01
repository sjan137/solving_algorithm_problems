import sys

# 페르마의 소정리 이용
# 소수인 p, p의 배수가 아닌 A에 대해 A^(p-1) === 1(mod p) - p로 나눈 나머지가 1
# 즉, (A^(p-2))%p = (A^(-1))%p
def fermaPower(b, p, origin_p):
    if p == 1: return b % origin_p
    elif p % 2: return (b * (fermaPower(b, p//2, origin_p) ** 2)) % origin_p
    else: return (fermaPower(b, p//2, origin_p) ** 2) % origin_p

def main():
    P = 1000000007
    N, K = map(int, sys.stdin.readline().split())
    # 재귀함수로 생성하면 재귀 반복 최대 횟수 초과 오류 발생
    factorialList = [1 for _ in range(N+1)]
    for i in range(2, N+1):
        factorialList[i] = (i * factorialList[i-1]) % P
    A, B = factorialList[N], factorialList[K]
    result = ((A%P) * (fermaPower(B, 1000000005, P)%P)) % P
    return result

if __name__ == "__main__":
    print(main())