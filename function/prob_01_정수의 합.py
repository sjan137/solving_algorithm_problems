def solve(a):
    n_sum = 0
    for a_num in a:
        try:
            n_sum += a_num
        except:
            pass
    return n_sum