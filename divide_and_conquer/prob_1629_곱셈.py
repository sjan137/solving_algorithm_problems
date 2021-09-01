import sys

# A, B, C를 입력으로 받는다.
# B가 1일 때는 A를 반환
# B가 짝수일 때 getPower(A, B//2, C) ** 2 후 c로 나눈 나머지 반환
# B가 홀수일 때 A * getPower(A^2, B//2, C) ** 2 후 c로 나눈 나머지 반환
def getPower(a, b, c):
    if b == 1: return a % c
    elif b % 2: return (a * getPower(a, b//2, c) ** 2) % c
    else: return (getPower(a, b//2, c) ** 2) % c

def main():
    A, B, C = list(map(int, sys.stdin.readline().split()))
    return getPower(A, B, C)

if __name__ == "__main__": print(main())