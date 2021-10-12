import sys

# 1. postorder의 마지막 숫자는 무조건 왼쪽 노드들과 오른쪽 노드들의 루트
# 2. postorder의 마지막 숫자와 같은 숫자를 기준으로 inorder에서 왼쪽, 오른쪽 노드들을 나눌 수 있음.
# 3. 나눈 노드들에 대해 같은(1번, 2번) 연산 수행 후 리턴
def get_preorder(inorder, postorder, i_start, p_start, i_end, p_end):
    if i_start > i_end or p_start > p_end: return []
    root_node = postorder[p_end]
    split_idx = inorder.index(root_node)
    return [root_node] + get_preorder(inorder, postorder, i_start, p_start, split_idx-1, split_idx-1) + get_preorder(inorder, postorder, split_idx+1, split_idx, i_end, p_end-1)

N = int(sys.stdin.readline())
inorders = list(map(int, sys.stdin.readline().split()))
postorders = list(map(int, sys.stdin.readline().split()))

print(*get_preorder(inorders, postorders, 0, 0, N-1, N-1))