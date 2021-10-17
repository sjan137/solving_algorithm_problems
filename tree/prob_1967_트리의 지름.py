import sys

# 1. 부모 노드, 자식 노드로 구분되어 입력이 주어지지만, 일반적인 트리로 구성(부모, 자식 구분 없는)
# 2. 연결된 노드가 1개뿐인 노드 하나를 골라서 DFS 수행, 방문하는 노드 저장
# 3. 해당 노드의 경우에서 가중치가 최대가 되는 경우, 가중치의 합과 방문한 노드의 마지막 노드 반환
# 4. 방문한 마지막 노드에 대해 DFS 수행
def DFS(tree_info, check, visit, start_node):
    max_w = 0
    visit = [start_node]
    for next_node, w in tree_info[start_node]:
        if check[next_node-1]: continue
        check[next_node-1] = True
        w_sum, new_visit = DFS(tree_info, check, [], next_node)
        if max_w < w + w_sum:
            max_w = w + w_sum
            visit += new_visit
        check[next_node-1] = False
    return max_w, visit

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))
checked = [False] * N
cur_node = 1

while len(tree[cur_node]) != 1:
    cur_node += 1

for _ in range(2):
    checked[cur_node-1] = True
    result, history = DFS(tree, checked, [], cur_node)
    checked[cur_node-1] = False
    cur_node = history[-1]

print(result)