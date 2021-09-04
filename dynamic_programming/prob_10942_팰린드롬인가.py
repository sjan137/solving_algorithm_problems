import sys

def isPal(data, idx):
    newData = data[idx[0]-1:idx[1]]
    n = idx[1] - idx[0] + 1
    # P = [[0] * n for _ in range(n)]
    
    # for i in range(n-2, -1, -1):
    #     for j in range(i+1, n):
    #         if newData[i] == newData[j]: P[i][j] = P[i+1][j-1]
    #         else: P[i][j] = min(P[i+1][j], P[i][j-1]) + 1
    
    # if P[0][-1]: return 0
    # else: return 1
    i, j = 0, n-1
    flag = False
    while not flag and i <= n // 2:
        flag = (newData[i] == newData[j])
        i += 1
        j -= 1

    if flag: return 1
    else: return 0

def main():
    N = int(sys.stdin.readline())
    nums = sys.stdin.readline().split()
    M = int(sys.stdin.readline())
    result = [isPal(nums, list(map(int, sys.stdin.readline().split()))) for _ in range(M)]
    return result

if __name__ == "__main__":
    print('\n'.join(map(str, main())))