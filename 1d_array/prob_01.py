# 최대, 최소 찾기
import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
print(min(num_list), max(num_list))