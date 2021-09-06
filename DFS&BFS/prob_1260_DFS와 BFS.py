import sys
from collections import deque

dfs_result = []
bfs_result = []

# DFS
def dfs(v, graph, visited):
    global dfs_result
    dfs_result.append(v)
    visited[v-1] = True

    for i in sorted(graph[v]):
        if not visited[i-1]: dfs(i, graph, visited)

# BFS
def bfs(v, graph, visited):
    global bfs_result
    q = deque([v])

    while q:
        vertex = q.popleft()
        if not visited[vertex-1]: bfs_result.append(vertex)
        visited[vertex-1] = True
        for i in sorted(graph[vertex]):
            if not visited[i-1]: q.append(i)

def main():
    global dfs_result, bfs_result
    N, M, V = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        idx1, idx2 = map(int, sys.stdin.readline().split())
        graph[idx1].append(idx2)
        graph[idx2].append(idx1)
    
    dfs(V, graph, [False] * N)
    bfs(V, graph, [False] * N)
    return (dfs_result, bfs_result)

if __name__ == "__main__":
    for line in main():
        print(' '.join(map(str, line)))