import sys


def main():
    N = int(sys.stdin.readline())
    time_list = list(map(int, sys.stdin.readline().split()))
    time_list.sort()

    for i in range(1, N):
        time_list[i] += time_list[i-1]
    
    print(sum(time_list))
    return None

if __name__ == "__main__":
    main()