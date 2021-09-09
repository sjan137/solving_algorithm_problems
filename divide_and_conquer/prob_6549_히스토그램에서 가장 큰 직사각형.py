import sys

def getRect(heights) :
    n = len(heights)
    if n == 1: return heights[0]
    mid = n // 2
    left_h = getRect(heights[:mid])
    right_h = getRect(heights[mid:])
    l = mid - 1
    r = mid
    under_w = 2
    min_h = min(heights[l], heights[r])
    max_area = under_w * min_h
    
    while 0 <= l and r + 1 <= n:
        lh = heights[l-1] if l >= 1 else 0
        rh = heights[r+1] if r < n-1 else 0
        min_h = min(min_h, lh) if lh > rh else  min(min_h, rh)
        if lh > rh: l -= 1
        else: r += 1
        under_w += 1
        max_area = max(max_area, under_w * min_h)
    
    return max(left_h, right_h, max_area)

def main():
    while True:
        heights = list(map(int, sys.stdin.readline().split()))
        if len(heights) == 1 and heights[0] == 0: break
        print(getRect(heights[1:]))

if __name__ == "__main__":
    main()