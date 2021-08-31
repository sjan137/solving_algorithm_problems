import sys

# 색종이를 나누고, 나눈 색종이의 각 개수를 반환
# 입력 받은 색종이가 단색이라면, (1, 0)-하양 또는 (0, 1)-파랑 형태로 반환
# 단색이 될 때까지 좌우로 나눔
def dividePaper(paper, n):
    result = []
    if n == 1 or isOneColor(paper):
        if paper[0][0] == 0: return [(1, 0)]
        else: return [(0, 1)]
    
    mid = n // 2
    d1 = [row[:mid] for row in paper[:mid]]
    d2 = [row[mid:] for row in paper[:mid]]
    d3 = [row[:mid] for row in paper[mid:]]
    d4 = [row[mid:] for row in paper[mid:]]

    for d in [d1, d2, d3, d4]:
        result += dividePaper(d, mid)
    return result

def isOneColor(paper):
    n = len(paper)
    ref = paper[0][0]
    
    for i in range(n):
        for j in range(n):
            if paper[i][j] != ref: return False
    return True

def main():
    N = int(sys.stdin.readline())
    color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    color_info = dividePaper(color_paper, N)
    white = 0
    blue = 0
    
    for w, b in color_info:
        white += w
        blue += b
    
    return white, blue

if __name__ == '__main__':
    w, b = main()
    print(w)
    print(b)