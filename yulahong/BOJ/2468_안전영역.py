from collections import deque

def bfs(x, y, h, visited, grid, n):
    queue = deque([(x, y)])
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

#  격자 정보
n = int(input())
grid = []
max_h = 0

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    max_h = max(max_h, max(row))

max_safe_zones = 1

for h in range(1, max_h):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):

            if grid[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited, grid, n)
                count += 1
    
    if count > max_safe_zones:
        max_safe_zones = count

print(max_safe_zones)