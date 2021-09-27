def solution(N, stages):
    M = len(stages)
    failure = []
    cnt = 0
    
    for i in range(1, N+1):
        M -= cnt
        cnt = stages.count(i)
        if cnt == 0: fail = 0
        else: fail = cnt / M
        failure.append((fail, i))
    
    failure.sort(key=lambda x: (-x[0], x[1]))
    answer = [x[1] for x in failure]
    
    return answer