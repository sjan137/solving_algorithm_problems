import sys

X = int(sys.stdin.readline())
sticks = [64]

while sum(sticks) > X:
    min_stick = sticks.pop() // 2
    if sum(sticks) + min_stick >= X:
        sticks.append(min_stick)
    else:
        sticks.append(min_stick)
        sticks.append(min_stick)

print(len(sticks))