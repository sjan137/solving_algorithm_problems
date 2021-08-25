import sys

# M개 중에서 (M-N)개를 순서 상관없이 선택하는 경우의 수 구하기
def combination(nm):
    n, m = nm
    n = min(n, m-n)
    result = 1

    for i in range(n):
        result = result * (m-i) / (i+1)
    
    return int(result)


def main():
    T = int(sys.stdin.readline())
    nm_list = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    
    for nm in nm_list:
        print(combination(nm))

    return None

if __name__ == '__main__':
    main()