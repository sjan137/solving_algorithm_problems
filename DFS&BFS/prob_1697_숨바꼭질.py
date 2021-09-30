import sys
from collections import deque

def BFS(n, k):
    if n == k: return 0
    max_len = 100001
    visited = [0] * max_len
    q = deque([n])

    while q:
        cur = q.popleft()
        can_visit = [cur-1, cur+1, cur*2]
        for i in can_visit:
            if (0 <= i < max_len) and not visited[i]:
                visited[i] = visited[cur] + 1
                if i == k: return visited[k]
                q.append(i)

N, K = map(int, sys.stdin.readline().split())
print(BFS(N, K))