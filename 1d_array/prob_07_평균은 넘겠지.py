import sys

T = int(sys.stdin.readline())
for t in range(T):
    test_case = list(map(int, sys.stdin.readline().split()))
    N = test_case.pop(0)
    case_mean = sum(test_case) / N
    high_count = 0
    for num in test_case:
        if num > case_mean: high_count += 1
    print('%0.3f%%' % ((high_count / N) * 100))