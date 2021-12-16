import sys


def getTeamCases(n, checked, team, start):
    global all_cases

    if sum(checked) == (n//2):
        all_cases.append(team)
        return
    
    for i in range(start, n):
        if checked[i]: continue
        checked[i] = True
        team.append(i)
        getTeamCases(n, checked, team[:], i+1)
        checked[i] = False
        team.pop()
    
    return


def getScoreDiff(team_a, n, s):
    team_b = [b for b in range(n) if b not in team_a]
    a_score = 0
    b_score = 0

    for i in team_a:
        for j in team_a:
            if i == j: continue
            a_score += s[i][j]

    for i in team_b:
        for j in team_b:
            if i == j: continue
            b_score += s[i][j]
    
    return abs(a_score - b_score)


N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [False] * N
all_cases = []
getTeamCases(N, check, [], 0)

min_diff = 9876543210
for case in all_cases:
    min_diff = min(min_diff, getScoreDiff(case, N, S))
    
print(min_diff)