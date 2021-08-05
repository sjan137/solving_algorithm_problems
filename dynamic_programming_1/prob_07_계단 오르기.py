import sys


def step_stairs(n, stairs_score, start):
    if start == n:
        score_sum_list.append(sum(score_sum))
        return None

    for i in range(2):
        if i == 0:
            if start < 2:
                if len(one_limit) == 2:
                    one_limit.pop()
                    one_limit.pop()
                    continue
                else:
                    one_limit.append(1)
            else:
                if one_limit:
                    one_limit.pop()
                    continue
                else:
                    one_limit.append(1)
        start += (i+1)
        if start > n: return None
        score_sum.append(stairs_score[start])
        step_stairs(n, stairs_score, start)
        start -= (i+1)
        score_sum.pop()
    return None

N = int(sys.stdin.readline())
stairs_score = [0] + [int(sys.stdin.readline()) for _ in range(N)]
one_limit = []
score_sum = []
score_sum_list = []
step_stairs(N, stairs_score, 0)
print(max(score_sum_list))