import sys

N = int(sys.stdin.readline())
words_dict = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    if word not in words_dict: words_dict[word] = len(word)

words_list = sorted(list(words_dict.items()), key=lambda x: (x[1], x[0]))
for wl in words_list:
    print(wl[0])