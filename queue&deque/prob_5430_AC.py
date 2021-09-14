import sys
from collections import deque

def AC(string_num, command, n):
    q = deque(map(int, string_num))
    reverseCnt = 0
    
    for c in command:
        if c == 'R': reverseCnt += 1
        elif c == "D":
            if not q: return 'error'
            if reverseCnt % 2 == 0: q.popleft()
            else: q.pop()
    
    if reverseCnt % 2 == 1: q.reverse()
    return "[" + ','.join(map(str, q)) + "]" 

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        command = sys.stdin.readline().strip()
        N = int(sys.stdin.readline())
        nums_str = sys.stdin.readline().strip()[1:-1].split(',')
        if N == 0 and 'D' in command: print('error')
        else: print(AC(nums_str, command, N)) if N != 0 else print('[]')
    return

if __name__ == "__main__":
    main()