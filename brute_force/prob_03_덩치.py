import sys

def decideRank(n, x_list, y_list):
    rank_result = list()
    for i in range(n):
        bigger_result = list()
        for j in range(n):
            if (x_list[i] < x_list[j]) and (y_list[i] < y_list[j]):
                bigger_result.append(True)
            else: bigger_result.append(False)
        rank_result.append(bigger_result.count(True) + 1)
    for _ in rank_result:
        print(_, end=' ')

N = int(sys.stdin.readline())
X = list()
Y = list()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
decideRank(N, X, Y)