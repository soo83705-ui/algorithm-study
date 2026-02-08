T = int(input())
dr = [0, 1, 0, -1]  # 우하좌상에서 "행(row)" 변화량
dc = [1, 0, -1, 0]  # 우하좌상에서 "열"변화량

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]  # 파리들이 살고 있는 곳의 범위
    max_sum_area = 0   #최대 합
    for r in range(N - M + 1):
        for c in range(N - M + 1):  # 기준점(r,c)을 정해서 파리채(M*M)가 움직일 수 있는 범위
            base = arr[r][c]

            sum_area = 0  # 파리채의 넓이합 초기화 상태

            for i in range(M):  # 파리채 내부의 기준점 (i,j)
                for j in range(M):
                    sum_area += arr[r + i][c + j]  # 파리채 안의 칸을 실제 격자 좌표로 바꾸는 공식

            if max_sum_area < sum_area:
                max_sum_area = sum_area

    print(f'#{tc} {max_sum_area}')