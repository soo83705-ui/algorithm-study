# 알파벳 소문자로 이루어진 N개의 단어를 조건에 따라 정렬
# 길이가 짧은 것부터
# 길이가 같다면 사전 순으로

# 변수
N = int(input())
word_lst = []

for _ in range(N):
    words = input()
    word_lst.append(words)

# 중복된 단어 제거 및 단어 사전순 정렬
rm_word_lst = list(set(word_lst))

# 단어 길이순 정렬
final_lst = sorted(rm_word_lst, key=lambda x: (len(x), x))

print('\n'.join(final_lst))

# 첫번째 접근
# word_lst 돌면서 길이 체크 후 정렬
# 인덱스랑 같이 저장

# 정렬된 후에 인덱스로 단어 꺼내오기
# 같은 것끼리 사전 순 비교 후 정렬
