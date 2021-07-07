import sys

X = int(sys.stdin.readline())
count = 0
acc_count = 0
while acc_count < X:
    count += 1
    acc_count += count
a = count
b = 1
diff = acc_count - X
if (a % 2) == 1: print('%d/%d' % (b + diff, a - diff))
else: print('%d/%d' % (a - diff, b + diff))