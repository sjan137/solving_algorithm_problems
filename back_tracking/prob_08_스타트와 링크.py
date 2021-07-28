import sys

def splitTeam(n, count):
    if count == n//2:
        stat_diff = abs(statSum(team1_list) - statSum(team2_list))
        stat_diff_result.append(stat_diff)
        return

    for i in range(n):
        if split_check[i]: continue
        split_check[:i+1] = [True] * (i+1)
        team1_list.append(i+1)
        team2_list.remove(i+1)
        splitTeam(n, count+1)
        split_check[:i+1] = [False] * (i+1)
        team1_list.pop()
        team2_list.append(i+1)

def statSum(team_list):
    stat_sum = 0

    if stat_sum_check.count(True) == 2:
        a, b = true_save
        return every_stat[a][b]
    
    for i in team_list:
        if stat_sum_check[i-1]: continue
        stat_sum_check[i-1] = True
        true_save.append(i-1)
        stat_sum += statSum(team_list)
        stat_sum_check[i-1] = False
        true_save.pop()
    
    return stat_sum

N = int(sys.stdin.readline())
every_stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
split_check = [False] * N
stat_sum_check = [False] * N
team1_list, team2_list = list(), list(range(1, N+1))
true_save, stat_diff_result = list(), list()
splitTeam(N, 0)
print(min(stat_diff_result))

# 1~N 중에 반을 선택(순서 상관 없이). 선택한 숫자와 선택하지 않은 숫자 리스트 생성하는 함수 구현
# 각 숫자 리스트를 입력하면 스탯 표에서 합을 추출하는 함수 구현