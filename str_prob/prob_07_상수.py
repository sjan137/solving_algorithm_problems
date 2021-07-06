import sys

a, b = sys.stdin.readline().split()
a, b = list(a), list(b)

a_reverse = '0'
b_reverse = '0'
while len(a) != 0:
    a_reverse += a.pop()
while len(b) != 0:
    b_reverse += b.pop()

a_reverse = int(a_reverse)
b_reverse = int(b_reverse)
if a_reverse > b_reverse: print(a_reverse)
else: print(b_reverse)