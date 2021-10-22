import sys

C = int(sys.stdin.readline())
for _ in range(C):
    N, M = map(int, sys.stdin.readline().split())
    check_odd = 0  # 홀수
    check_even = 0  # 짝수
    for _ in range(N):
        row = sys.stdin.readline()
        for i in range(M):
            if (i+1) % 2:
                if row[i] == '.': check_odd += 1
            else:
                if row[i] == '.': check_even += 1
    print(max(check_odd, check_even))