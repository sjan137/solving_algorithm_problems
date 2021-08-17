import sys


def main():
    N = int(sys.stdin.readline())
    time_schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 람다와 튜플, sort의 key 속성을 이용해서 끝나는 시간에 대해 먼저 오름차순 정렬, 같다면 시작하는 시간에 대해 오름차순 정렬 진행
    time_schedule.sort(key=lambda x: (x[1], x[0]))
    
    greedy = 0
    greedy_ref = 0
    
    for i in range(N):
        if time_schedule[i][0] >= greedy_ref:
            greedy_ref = time_schedule[i][1]
            greedy += 1
    
    print(greedy)
    return None

if __name__ == '__main__':
    main()