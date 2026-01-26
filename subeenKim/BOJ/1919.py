first_w = input().strip()
second_w = input().strip()

first_w = list(first_w)
second_w = list(second_w)

inter = set(first_w) & set(second_w)
words_cnt = len(first_w) + len(second_w)

for i in inter :
    cnt = min(first_w.count(i), second_w.count(i))
    words_cnt -= cnt*2

print(words_cnt)