import sys

def main():
    while True:
        sentence = sys.stdin.readline().rstrip()
        if sentence == '.': break
        print(isBalance(sentence))

    return

def isBalance(words):
    st = []
    for digit in words:
            if digit == "(": st.append(1)
            if digit == "[": st.append(2)
            elif digit == ")":
                if st and st[-1] == 1: st.pop()
                else: return 'no'
            elif digit == "]":
                if st and st[-1] == 2: st.pop()
                else: return 'no'
    if st: return 'no'
    return 'yes'

if __name__ == "__main__":
    main()