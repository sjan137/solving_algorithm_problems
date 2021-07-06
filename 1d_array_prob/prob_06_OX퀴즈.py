import sys

T = int(sys.stdin.readline())
for i in range(T):
    score = 0
    test_case = list(sys.stdin.readline().split('X'))
    for o_case in test_case:
        o_count = o_case.count('O')
        n = 1
        while n <= o_count:
            score += n
            n += 1
    print(score)