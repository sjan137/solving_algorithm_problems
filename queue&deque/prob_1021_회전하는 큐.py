import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().split())
    picks = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    q = deque(range(1, N+1))

    for p in picks:
        tempCnt = 0
        while q[0] != p:
            q.rotate()
            tempCnt += 1
        cnt += min(tempCnt, N-tempCnt)
        N -= 1
        q.popleft()
    
    return cnt

if __name__ == "__main__":
    print(main())