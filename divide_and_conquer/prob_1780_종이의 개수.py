import sys

# 종이 정보, 열 개수(n)를 입력으로 받음.
# n == 1이거나 단일색으로 이루어진 종이일 때 [(0, 0, 0)] 형태로 반환
# 색이 다르면 9등분으로 나누고 다시 진행
counts = [0] * 3

def countPaper(paper, x, y, n):
    global counts
    pivot = paper[y][x]
    if n == 1:
        counts[pivot] += 1
        return
    tri = n // 3

    for i in range(y, y+n):
        for j in range(x, x+n):
            if pivot != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        countPaper(paper, x+tri*b, y+tri*a, tri)
                return
    counts[pivot] += 1
    return

def main():
    global counts
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    countPaper(arr, 0, 0, N)
    
    return counts

if __name__ == "__main__":
    result = main()
    print(result[-1])
    for i in result[:-1]:
        print(i)