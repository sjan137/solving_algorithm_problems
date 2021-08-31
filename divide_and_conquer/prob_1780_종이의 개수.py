import sys

# 종이 정보, 열 개수(n)를 입력으로 받음.
# n == 1이거나 단일색으로 이루어진 종이일 때 [(0, 0, 0)] 형태로 반환
# 색이 다르면 9등분으로 나누고 다시 진행
def countPaper(paper, x, y, n):
    result = []
    pivot = paper[y][x]
    result_dict = {-1: (1, 0, 0), 0: (0, 1, 0), 1: (0, 0, 1)}
    if n == 1: return [result_dict[pivot]]
    tri = n // 3
    split_cases = [[x, y], [x+tri, y], [x+2*tri, y], [x, y+tri], [x+tri, y+tri], [x+2*tri, y+tri], [x, y+2*tri], [x+tri, y+2*tri], [x+2*tri, y+2*tri]]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if pivot != paper[i][j]:
                for xx, yy in split_cases:
                    result += countPaper(paper, xx, yy, tri)
                return result
    return [result_dict[pivot]]

def main():
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    counts = countPaper(arr, 0, 0, N)
    minus_one = 0
    zero = 0
    one = 0

    for a, b, c in counts:
        minus_one += a
        zero += b
        one += c
    
    return minus_one, zero, one

if __name__ == "__main__":
    a, b, c = main()
    print(a)
    print(b)
    print(c)