import sys


def isVPS(ps):
    result = []
    for digit in ps:
        if digit == "(": result.append(1)
        else:
            if len(result) == 0: return "NO"
            else: result.pop()
    if result: return "NO"
    return "YES"

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for digit in range(T):
        ps = sys.stdin.readline().strip()
        print(isVPS(ps))