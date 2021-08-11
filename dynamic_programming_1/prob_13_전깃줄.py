import sys

# 무작위로 입력된 전깃줄의 순서를 왼쪽 라인에 맞추어 먼저 정렬.
def solve(n, cables):
    numbering = [0] * 500
    sorted_cable = []
    result = [0] * n

    for i in range(n):
        x = cables[i][0]
        numbering[x-1] = i+1

    for i in range(500):
        if not numbering[i]: continue
        sorted_cable.append(cables[numbering[i]-1])
    
    for i in range(n):
        a, b = sorted_cable[i]
        for j in range(i):
            aa, bb = sorted_cable[j]
            if aa < a and bb < b:
                if result[j] > result[i]: result[i] = result[j]
        result[i] += 1
    return n-max(result)

N = int(sys.stdin.readline())
elec_cable = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solve(N, elec_cable))