import sys

words = list(sys.stdin.readline().strip().upper())
alpha_count = list()
unique_words = list(set(words))
for alphabet in unique_words:
    alpha_count.append(words.count(alphabet))
if alpha_count.count(max(alpha_count)) >= 2: print('?')
else: print(unique_words[alpha_count.index(max(alpha_count))])