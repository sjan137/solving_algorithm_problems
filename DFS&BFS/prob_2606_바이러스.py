import sys
from collections import deque

def BFS(graph, n):
    visited = [False] * (n+1)
    q = deque([1])
    cnt = -1

    while q:
        node = q.popleft()
        for elem in graph[node]:
            if not visited[elem]:
                q.append(elem)
                visited[elem] = True
                cnt += 1
    
    return cnt

def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        line = list(map(int, sys.stdin.readline().split()))
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    return BFS(graph, N)

if __name__ == "__main__":
    print(main())