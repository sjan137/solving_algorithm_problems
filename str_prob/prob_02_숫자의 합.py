import sys

N = int(sys.stdin.readline())
num_list = [int(x) for x in sys.stdin.readline().replace('', ' ').split()]
print(sum(num_list))