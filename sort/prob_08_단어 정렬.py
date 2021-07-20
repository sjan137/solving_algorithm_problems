import sys

def word_sort(word_hash):
    for i in range(51):
        if i in word_hash.keys():
            word_hash[i].sort(reverse=True)
            while len(word_hash[i]) != 0:
                print(word_hash[i].pop())
        else: continue

N = int(sys.stdin.readline())
# 단어의 길이를 key 값으로 하며 저장하는 딕셔너리 생성
word_hash = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    w_key = len(word)
    if w_key in word_hash.keys():
        if word in word_hash[w_key]: continue
        else: word_hash[w_key].append(word)
    else: word_hash[w_key] = [word]
word_sort(word_hash)