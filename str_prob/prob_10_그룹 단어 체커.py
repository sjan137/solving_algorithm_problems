import sys

N = int(sys.stdin.readline())
count = 0
for n in range(N):
    word = sys.stdin.readline().strip()
    word_set = set(word)
    for alpha in word_set:
        alpha_count = word.count(alpha)
        if alpha * alpha_count in word:
            word = word.replace(alpha * alpha_count, alpha)
    if len(word) == len(word_set): count += 1
print(count)