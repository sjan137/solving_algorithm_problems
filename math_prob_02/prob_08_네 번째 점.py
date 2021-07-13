import sys


a_list = list()
b_list = list()
for t in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if a in a_list: a_list.remove(a)
    else: a_list.append(a)
    if b in b_list: b_list.remove(b)
    else: b_list.append(b)
print(a_list[0], b_list[0])