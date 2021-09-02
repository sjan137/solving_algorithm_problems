import sys

def main():
    N = int(sys.stdin.readline())
    st_list = [int(sys.stdin.readline()) for _ in range(N)]
    st = []
    result = []
    cur_num = 1

    for i in range(N):
        while st_list[i] >= cur_num:
            st.append(cur_num)
            result.append('+')
            cur_num += 1
        if st[-1] == st_list[i]:
            st.pop()
            result.append('-')
        else: return ['NO']
    return result

if __name__ == "__main__":
    for i in main():
        print(i)