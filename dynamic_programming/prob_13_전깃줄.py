import sys

# 무작위로 입력된 전깃줄을 왼쪽을 키, 오른쪽을 값으로 하는 딕셔너리로 설정 후 빠른 색인을 통해 구하기
def solve(n, cables):
    cable_hash = {}
    count = [0] * n
    for cable in cables:
        x, y = cable
        cable_hash[x] = y

    x_list = list(cable_hash.keys())
    x_list.sort()

    for i in range(n):
        x = x_list[i]
        y = cable_hash[x]
        for j in range(i):
            xx = x_list[j]
            yy = cable_hash[xx]
            if y > yy:
                if count[j] > count[i]: count[i] = count[j]
        count[i] += 1
    return n - max(count)

N = int(sys.stdin.readline())
elec_cable = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solve(N, elec_cable))