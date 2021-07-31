import sys

# 결과를 순열의 합으로 계산
def binaryTile(n):
    global count
    if n == 1: return
    a = n - 1
    b = 1
    while a >= b:
        count += combination(a, b)
        a -= 1
        b += 1
    return(count)

def combination(a, b):
    result = 1
    c = a - b
    for i in range(b, a):
        result *= (i+1)
    while c > 0:
        result /= c
        c -= 1
    return int(result)

N = int(sys.stdin.readline())
count = 1
print(binaryTile(N))