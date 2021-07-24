import sys

def nQueen(start, n):
    if len(result) == n:
        print(result)
        count.append(1)
        return
    else:
        for i in range(n):
            if check[start][i]: continue
            result.append(i+1)
            temp_check = check
            # len_rst = len(result)
            # for j in result:
            #     row_list = [j-1-len_rst, j-1, j-1+len_rst]
            #     for k in row_list:
            #         if (k < 0) or (k > n-1) or check[k]: continue
            #         check[k] = True
            check[i] = True
            nQueen(start+1, n)
            check[i] = False
            result.pop()

N = int(sys.stdin.readline())
result = list()
check = [[False] * N] * N
count = list()
nQueen(0, N)
print(len(count))