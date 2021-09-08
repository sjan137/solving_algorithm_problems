import sys

class LinkedListElement:
    def __init__(self, val,  p, n):
        self.value = val
        self.prev = p
        self.next = n

class Queue:

    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0
    
    def push(self, x):
        if self.empty():
            elem = LinkedListElement(x, None, None)
            self.start = self.end = elem
        else:
            elem = LinkedListElement(x, self.end, None)
            self.end.next = elem
            self.end = elem
        self.count += 1
        return
    
    def pop(self):
        if self.empty(): return -1
        elif self.size() == 1:
            start = self.start.value
            self.start = self.end = None
        else:
            start = self.start.value
            startNext = self.start.next
            self.start = startNext
            self.start.prev = None
        self.count -= 1
        return start
    
    def size(self):
        return self.count
    
    def empty(self):
        if self.count == 0: return 1
        return 0
    
    def front(self):
        if self.empty(): return -1
        return self.start.value
    
    def back(self):
        if self.empty(): return -1
        return self.end.value

def main():
    N = int(sys.stdin.readline())
    q = Queue()
    for _ in range(N):
        command = sys.stdin.readline().split()
        if command[0] == 'push': q.push(int(command[1]))
        elif command[0] == 'pop': print(q.pop())
        elif command[0] == 'size': print(q.size())
        elif command[0] == 'empty': print(q.empty())
        elif command[0] == 'front': print(q.front())
        elif command[0] == 'back': print(q.back())
    return

if __name__ == "__main__":
    main()