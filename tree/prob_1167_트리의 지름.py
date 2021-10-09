import sys
from collections import deque

V = int(sys.stdin.readline())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    nodes = deque(list(map(int, sys.stdin.readline().split())))
    idx = nodes.popleft()
    while nodes[0] != -1:
        node = nodes.popleft()
        distance = nodes.popleft()
        tree[idx].append((node, distance))

print(tree)