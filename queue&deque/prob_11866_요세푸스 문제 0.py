import sys
from collections import deque

def main():
    N, K = map(int, sys.stdin.readline().split())
    people = deque(range(1, N+1))
    result = []
    
    while people:
        for _ in range(K):
            people.append(people.popleft())
        result.append(people.pop())
    
    return result

if __name__ == "__main__":
    print("<" + ", ".join(map(str, main())) + ">")