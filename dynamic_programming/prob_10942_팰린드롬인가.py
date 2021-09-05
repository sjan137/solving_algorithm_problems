import sys

# 팰린드롬 여부를 저장하는 2차원 리스트. i == j인 경우는 모두 1
# data[i] == data[j]일 때, data[i+1] 부터 data[j-1]까지가 팰린드롬이라면(pal[i+1][j-1] == 1) i, j일 때도 팰린드롬
# data[i] != data[j]일 때, 팰린드롬 아님
def isPal(data):
    n = len(data)
    pal = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j: pal[i][j] = 1
            elif data[i] == data[j]:
                if pal[i+1][j-1]: pal[i][j] = 1
    
    return pal

def main():
    N = int(sys.stdin.readline())
    nums = sys.stdin.readline().split()
    M = int(sys.stdin.readline())
    pal_arr = isPal(nums)
    
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        print(pal_arr[start-1][end-1])
    return

if __name__ == "__main__":
    main()