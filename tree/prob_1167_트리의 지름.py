import sys
from collections import deque

# 1. 임의의 노드 1에서 DFS 탐색으로 최대 깊이 구하기
# 2. 1에서 시작했을 때 가장 긴 지름을 저장하고, 이 경우의 마지막 노드 반환
# 3. 마지막 노드에 대해 한 번 더 DFS 탐색하고, 두 경우의 지름 중 높은 지름을 출력
def DFS(tree_info, checked, start_node):
    max_depth = 0
    history = [start_node]
    next_nodes = tree_info[start_node]

    for next_node, dist in next_nodes:
        if checked[next_node-1]: continue
        checked[next_node-1] = True
        depth, next_history = DFS(tree_info, checked, next_node)
        if max_depth < dist + depth:
            max_depth = dist + depth
            history = history + next_history
        # max_depth = max(max_depth, dist + DFS(tree_info, checked, next_node))
        checked[next_node-1] = False
    
    return max_depth, history

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
start = 1

for _ in range(2):
    checked[start-1] = True
    result, visited = DFS(tree, checked, start)
    checked[start-1] = False
    start = visited[-1]

print(result)