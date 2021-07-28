import sys

def splitTeam(n, count):
    global min_stat_diff

    if count == n//2:
        stat_diff = abs(statSum(n, team1_list) - statSum(n, team2_list))
        if not min_stat_diff: min_stat_diff.append(stat_diff)
        else:
            if min_stat_diff[0] > stat_diff: min_stat_diff[0] = stat_diff
        return

    for i in range(n):
        if split_check[i]: continue
        split_check[:i+1] = [True] * (i+1)
        team1_list[i] = True
        team2_list[i] = False
        splitTeam(n, count+1)
        split_check[:i+1] = [False] * (i+1)
        team1_list[i] = False
        team2_list[i] = True

def statSum(n, team_list):
    stat_sum = 0

    if len(true_save) == 2:
        a, b = true_save
        return every_stat[a][b] + every_stat[b][a]
    
    for i in range(n):
        if not team_list[i]: continue
        else:
            if stat_sum_check[i]: continue
            stat_sum_check[:i+1] = [True] * (i+1)
            true_save.append(i)
            stat_sum += statSum(n, team_list)
            stat_sum_check[:i+1] = [False] * (i+1)
            true_save.pop()
    
    return stat_sum

N = int(sys.stdin.readline())
every_stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
split_check = [False] * N
stat_sum_check = [False] * N
team1_list, team2_list = [False] * N, [True] * N
true_save, min_stat_diff = list(), list()
splitTeam(N, 0)
print(min_stat_diff[0])

# 1~N 중에 반을 선택(순서 상관 없이). 선택한 숫자와 선택하지 않은 숫자 리스트 생성하는 함수 구현
# 각 숫자 리스트를 입력하면 스탯 표에서 합을 추출하는 함수 구현