import sys

def getCount(n, col, row, r_d, l_d):
    cnt = 0
    if col == n: return 1
    for i in range(n):
        if row[i] + r_d[col+i] + l_d[(n-1)+(col-i)]: continue
        row[i] = r_d[col+i] = l_d[(n-1)+(col-i)] = True
        cnt += getCount(n, col+1, row, r_d, l_d)
        row[i] = r_d[col+i] = l_d[(n-1)+(col-i)] = False
    return cnt

N = int(sys.stdin.readline())
rows = [False] * N
r_diagonal = [False] * (2*N-1)
l_diagonal = [False] * (2*N-1)
print(getCount(N, 0, rows, r_diagonal, l_diagonal))

# import sys

# def logic(n):
#     if n == N:
#         global count
#         count += 1
#     else:
#         for i in range(N):
#             if visited[i]: continue
#             board[n] = i
#             if check(n):
#                 visited[i]= True
#                 logic(n+1)
#                 visited[i] = False

# def check(n):
#     for i in range(n):
#         if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])): return False
#     return True

# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     count = 0
#     board = [0 for _ in range(N)]
#     visited = [False for _ in range(N)]

#     logic(0)
#     print(count)