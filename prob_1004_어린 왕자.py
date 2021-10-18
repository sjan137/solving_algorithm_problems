import sys

def underDist(start, end, xyr_list):
    result = []
    for x, y, r in xyr_list:
        if getDist(start, end, x, y) < r: result.append((x, y, r))
    return result

def getDist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

T = int(sys.stdin.readline())
for _ in range(T):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    start_set = set(underDist(start_x, start_y, points))
    end_set = set(underDist(end_x, end_y, points))
    count = len(start_set) + len(end_set) - 2 * len(start_set & end_set)
    print(count)