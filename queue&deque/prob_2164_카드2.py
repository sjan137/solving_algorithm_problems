import sys
from collections import deque

def main():
    cards = deque(range(1, int(sys.stdin.readline())+1))
    while len(cards) != 1:
        toRemove = cards.popleft()
        toLast = cards.popleft()
        cards.append(toLast)
    return cards[0]

if __name__ == "__main__":
    print(main())