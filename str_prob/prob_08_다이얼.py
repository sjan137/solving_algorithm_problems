import sys

str_list = list(sys.stdin.readline().strip())
dial_time = 0
for alpha in str_list:
    ref = ord(alpha)
    if ref < 80:
        dial_time += ((ref - 59) // 3) + 1
    elif ref == 87:
        dial_time += 9 + 1
    else:
        dial_time += ((ref - 52) // 4) + 1
print(dial_time)