import sys
from collections import deque

def knight(l, start, end):
    if start == end: return 0
    q = deque([start])
    end_i, end_j = end
    checked = [[0] * l for _ in range(l)]
    dr = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
    
    while not checked[end_i][end_j]:
        cur_i, cur_j = q.popleft()
        for di, dj in dr:
            i, j = cur_i+di, cur_j+dj
            if 0 <= i < l and 0 <= j < l and not checked[i][j]:
                q.append([i, j])
                checked[i][j] = checked[cur_i][cur_j] + 1
    
    return checked[end_i][end_j]

T = int(sys.stdin.readline())
for _ in range(T):
    l = int(sys.stdin.readline())
    cur_i, cur_j = map(int, sys.stdin.readline().split())
    i, j = map(int, sys.stdin.readline().split())
    print(knight(l, [cur_i, cur_j], [i, j]))