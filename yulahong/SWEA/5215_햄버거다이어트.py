# 칼로리 넘지 않게 > 조건
# 고객이 원하는 조합으로
# 칼로리 이하
# 가장 선호하는 조합 > 높은 점수

# 첫줄: 재료의 수 제한 칼로리
# 다음 N개의 줄에는 각 재료에 대한  민기의 점수 칼로리

T = int(input())
for tc in range(1, T+1):

    info_lst = []
    ham_set_lst = []

    N, L = map(int, input().split())

    for _ in range(N):
        score, calorie = map(int, input().split())
        info_lst.append((score, calorie))

    def ham_set(cnt, cs, cc):
        print(ham_set_lst)

        for i in range(prev, len(info_lst)):
            

