import sys

def recurW(a, b, c):
    if a <= 0 or b <= 0 or c<= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return recurW(20, 20, 20)

    elif a < b and b < c:
        return recurW(a, b, c-1) + recurW(a, b-1, c-1) - recurW(a, b-1, c)
    
    else:
        return recurW(a-1, b, c) + recurW(a-1, b-1, c) + recurW(a-1, b, c-1) - recurW(a-1, b-1, c-1)

# dynamic programming W
def dpW(a, b, c):
    if a <= 0 or b <= 0 or c<= 0:
        a = b = c = 0
    elif a > 20 or b > 20 or c> 20:
        a = b = c = 20
    
    # val = [[[0] * (c+1)] * (b+1)] * (a+1)
    val = []
    a += 1
    b += 1
    c += 1
    for i in range(a):
        for j in range(b):
            for k in range(c):
                p = i * (b) * (c)
                q = j * (c)
                r = k
                if i == 0 or j == 0 or k == 0: val.append(1)
                elif i < j and j < k: val.append(val[p + q + r-1] + val[p + q-c + r-1] - val[p + q-c + r])
                else: val.append(val[p-b*c + q + r] + val[p-b*c + q-c + r] + val[p-b*c + q + r-1] - val[p-b*c + q-c + r-1])
    # print(len(val), val)
    return val.pop()

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1: break
    # print(recurW(a, b, c))
    print(dpW(a, b, c))