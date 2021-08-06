import sys


def solve(n):
    count = [0] * n
    num_list = []
    min_count = 2

    if n >= 2:
        count[1] = 1
        num_list.append(2)
    if n >= 3:
        count[2] = 1
        num_list.append(3)
    
    while num_list:
        new_set = set()
        for i in num_list:
            a, b, c = i+1, i*2, i*3
            for j in [a, b, c]:
                if j > n or count[j-1]: continue
                else:
                    count[j-1] = min_count
                    new_set.add(j)
        num_list = list(new_set)
        min_count += 1
    return count[-1]

N = int(sys.stdin.readline())
print(solve(N))