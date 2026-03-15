# 탈주범이 있을 수 있는 위치의 개수 계산
# 시간당 1의 거리 움직임
 
from collections import deque
 
# 변수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
dict = { 1 : [0, 1, 2, 3],
    2 : [0, 1],
    3 : [2, 3],
    4 : [0, 3],
    5 : [1, 3],
    6 : [1, 2],
    7 : [0, 2] }
 
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # 세로크기, 가로크기, 맨홀위치, 소요시간
    arr = [list(map(int, input().split())) for _ in range(N)] # 지도
    visited = [[0]*M for _ in range(N)]
 
    q = deque()
    q.append((R, C))
    visited[R][C] = 1
 
    while q:
        cr, cc = q.popleft()
 
        for dir in dict[arr[cr][cc]]:
            nr = cr + dr[dir]
            nc = cc + dc[dir]
 
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 or visited[nr][nc] != 0:
                    continue
                if dir == 0:
                    if 1 not in dict[arr[nr][nc]]:
                        continue
                elif dir == 1:
                    if 0 not in dict[arr[nr][nc]]:
                        continue
                elif dir == 2:
                    if 3 not in dict[arr[nr][nc]]:
                        continue
                else:
                    if 2 not in dict[arr[nr][nc]]:
                        continue
 
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] <= L and visited[i][j] != 0:
                cnt += 1
 
    print(f'#{tc} {cnt}')