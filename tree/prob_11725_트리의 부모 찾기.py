import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
checked = [False] * N
result = [0] * (N-1)
q = deque([1])

for _ in range(N-1):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    tree[node_1].append(node_2)
    tree[node_2].append(node_1)

while q:
    parent = q.popleft()
    checked[parent-1] = True
    for child in tree[parent]:
        if checked[child-1]: continue
        q.append(child)
        result[child-2] = parent

for i in result:
    print(i)