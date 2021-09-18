import sys, heapq

def main():
    N = int(sys.stdin.readline())
    hq = []
    for _ in range(N):
        command = int(sys.stdin.readline())
        if command: heapq.heappush(hq, -command)
        else: print(-heapq.heappop(hq)) if hq else print(0)
    return

if __name__ == "__main__":
    main()