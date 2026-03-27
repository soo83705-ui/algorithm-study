from collections import deque

def bfs(R, C):
    queue = deque([(R, C)])
    visited[R][C] = True

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if area[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    area = [[0]*M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        # if 0 <= a < M and 0 <= b < N:
        area[b][a] = 1

    visited = [[False]*M for _ in range(N)]

    answer = 0

    for r in range(N):
        for c in range(M):
            if area[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                answer += 1

    print(answer)

