import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def rmpop(self):
        if self.stack: self.stack = self.stack[:-1]

    def pop(self):
        if self.stack: return self.stack.pop()
        else: return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack: return 0
        else: return 1
    
    def top(self):
        if self.stack: return self.stack[-1]
        else: return -1

def main():
    K = int(sys.stdin.readline())
    st = Stack()
    for _ in range(K):
        say = int(sys.stdin.readline())
        if say == 0: st.rmpop()
        else: st.push(say)
    result = sum(st.stack)

    return result

if __name__ == '__main__':
    print(main())