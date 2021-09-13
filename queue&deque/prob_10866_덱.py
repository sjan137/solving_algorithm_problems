import sys
from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()
    
    def push_front(self, x):
        self.dq.appendleft(x)
    
    def push_back(self, x):
        self.dq.append(x)
    
    def pop_front(self):
        print(self.dq.popleft()) if self.dq else print(-1)
    
    def pop_back(self):
        print(self.dq.pop()) if self.dq else print(-1)
    
    def size(self):
        print(len(self.dq))
    
    def empty(self):
        print(0) if self.dq else print(1)
    
    def front(self):
        print(self.dq[0]) if self.dq else print(-1)

    def back(self):
        print(self.dq[-1]) if self.dq else print(-1)

def main():
    N = int(sys.stdin.readline())
    dq = Deque()
    for _ in range(N):
        command = list(sys.stdin.readline().split())
        if command[0] == 'push_front': dq.push_front(command[1])
        elif command[0] == 'push_back': dq.push_back(command[1])
        elif command[0] == 'pop_front': dq.pop_front()
        elif command[0] == 'pop_back': dq.pop_back()
        elif command[0] == 'size': dq.size()
        elif command[0] == 'empty': dq.empty()
        elif command[0] == 'front': dq.front()
        elif command[0] == 'back': dq.back()
    return

if __name__ == "__main__":
    main()