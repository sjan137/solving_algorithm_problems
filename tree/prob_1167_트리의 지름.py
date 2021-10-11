import sys
from collections import deque

# 1. 연결된 노드의 개수가 1이라면(끝 노드), 탐색 시작
# 2. DFS 탐색으로 최대 깊이 구하기
def DFS(tree_info, checked, start_node):
    max_depth = 0
    next_nodes = tree_info[start_node]
    for next_node, dist in next_nodes:
        if checked[next_node-1]: continue
        checked[next_node-1] = True
        max_depth = max(max_depth, dist+DFS(tree_info, checked, next_node))
        checked[next_node-1] = False
    return max_depth

V = int(sys.stdin.readline())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    nodes = deque(list(map(int, sys.stdin.readline().split())))
    idx = nodes.popleft()
    while nodes[0] != -1:
        node = nodes.popleft()
        distance = nodes.popleft()
        tree[idx].append((node, distance))
checked = [False] * V
result = 0

for i in range(1, V+1):
    if len(tree[i]) != 1: continue
    checked[i-1] = True
    result = max(result, DFS(tree, checked, i))
    checked[i-1] = False

print(result)