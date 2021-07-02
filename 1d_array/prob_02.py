# prob_02_최대값과 위치 반환
import sys

ref = 0
ref_list = [0, 0]
for i in range(9):
    n = int(sys.stdin.readline())
    if ref < n:
        ref_list[0], ref_list[1] = n, i+1
        ref = n
print('%s\n%s' % (ref_list[0], ref_list[1]))