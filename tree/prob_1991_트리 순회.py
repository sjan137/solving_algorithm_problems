import sys

# 전위 순회
def preorder(tree, root_node):
    if root_node == '.': return ''
    left_node, right_node = tree[root_node]
    return root_node + preorder(tree, left_node) + preorder(tree, right_node)

# 중위 순회
def inorder(tree, root_node):
    if root_node == '.': return ''
    left_node, right_node = tree[root_node]
    return inorder(tree, left_node) + root_node + inorder(tree, right_node)

# 후위 순회
def postorder(tree, root_node):
    if root_node == '.': return ''
    left_node, right_node = tree[root_node]
    return postorder(tree, left_node) + postorder(tree, right_node) + root_node

tree_dict = {}
N = int(sys.stdin.readline())
for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree_dict[root] = [left, right]

print(preorder(tree_dict, 'A'))
print(inorder(tree_dict, 'A'))
print(postorder(tree_dict, 'A'))