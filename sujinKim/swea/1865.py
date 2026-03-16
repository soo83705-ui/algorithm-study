# import sys
# sys.stdin = open('input.txt')

def recur(index,possible):  # 함수
    global result
    # global solution

    if result >= possible: # 결과값이 값보다 보관하는곳의 합이 작다면
        # solution = 0
        return # 함수를 빠져나옴

    if index == N: # 끝 열까지 방문을 다 했을때
        # tmp = 100.0    # 100을 곱하는 것의 역할
        #
        # for sol in solution:
        #     tmp *= sol


        result = max(result,possible)
        return # 함수를 빠져나옴

    for i in range(N):
        if not visited[i]:  ##??맞나??


            # solution[index] = arr[index][i]/100  # solution 리스트에 들어가는 각각의 값들을 100으로 나눴던 것을 넣는다.
            visited[i] = True
            recur(index+1, possible*arr[index][i]/100)
            visited[i] = False   # 원복

            # solution[index] = 0  # 원복


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [False]*N    # 각 열에 방문 했는지 안했는지
    result = float("-inf")  # 최대값을 구하기 위해 비교할 대상

    # solution = [0]*N # 각 열마다 값을 골라서 넣는곳


    recur(0,100)

    print(f"#{tc} {result:.6f}")






