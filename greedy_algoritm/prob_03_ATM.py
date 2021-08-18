import sys


def main():
    N = int(sys.stdin.readline())
    time_list = list(map(int, sys.stdin.readline().split()))
    time_list.sort()

    time_sum = 0
    for i in range(N):
        time_sum += time_list[i] * (N - i)
    
    print(time_sum)
    return None

if __name__ == "__main__":
    main()