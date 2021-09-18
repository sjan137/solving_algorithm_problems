import sys, heapq

def main():
    N = int(sys.stdin.readline())
    hq = []
    for _ in range(N):
        x = int(sys.stdin.readline())
        heapq.heappush(hq, (abs(x), x)) if x else (print(heapq.heappop(hq)[1]) if hq else print(0))
    return

if __name__ == "__main__":
    main()