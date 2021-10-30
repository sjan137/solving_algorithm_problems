import sys

def check(n):
    m = list(n)
    new_m = list(reversed(m))
    
    if m == new_m: print("yes")
    else: print('no')

while True:
    N = sys.stdin.readline().strip()
    if N == '0': break
    check(N)