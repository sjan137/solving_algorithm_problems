import sys

# 재귀 함수로 풀어본 버전
def solve(n, n_list, start):
    if start == (n-1):
        if len(temp) > result[0]: result[0] = len(temp)
    
    if not temp: temp.append(n_list[start])
    for i in range(start+1, n):
        if temp[-1] >= n_list[i]: continue
        temp.append(n_list[i])
        solve(n, n_list, i)
        temp.pop()
    return

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
temp = []
result = [0]
solve(N, num_list, 0)
print(result[0])