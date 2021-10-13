import sys
sys.setrecursionlimit(10**9)

# 1. postorder의 마지막 숫자는 무조건 왼쪽 노드들과 오른쪽 노드들의 루트이므로 먼저 출력
# 2. inorder에서 postorder의 마지막 숫자와 일치하는 자리의 인덱스 숫자를 split_idx에 저장
# 3. 해당 인덱스를 기준으로 나뉘는 양쪽의 개수, 길이(left_len, right_len)를 구해서 각 범위만큼 왼쪽, 오른쪽을 다시 재귀 호출
N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
idx_list = [0] * (N+1)
for i in range(N):
    idx_list[inorder[i]] = i

def get_preorder(i_start, p_start, i_end, p_end):
    if (i_start > i_end) or (p_start > p_end): return []
    root_node = postorder[p_end]
    print(root_node, end=' ')
    split_idx = idx_list[root_node]
    left_len = split_idx - i_start
    right_len = i_end - split_idx
    get_preorder(i_start, p_start, i_start+left_len-1, p_start+left_len-1)
    get_preorder(i_end-right_len+1, p_end-right_len, i_end, p_end-1)

get_preorder(0, 0, N-1, N-1)