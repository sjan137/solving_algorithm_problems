import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

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


def doStack(order_list):
    st = Stack()
    for order in order_list:
        if order == "pop": print(st.pop())
        elif order == 'size': print(st.size())
        elif order == 'empty': print(st.empty())
        elif order == 'top': print(st.top())
        else:
            num = int(order.split()[1])
            st.push(num)

N = int(sys.stdin.readline())
orders = [sys.stdin.readline().strip() for _ in range(N)]
doStack(orders)