# 변수
# N = int(input())
# visited > visited = [[0]*N for _ in range(N)]


dr = [1, 1, 1]
dc = [-1, 1, 0]

N = int(input())
visited = [[10**9]*N for _ in range(N)]
count = 0

def dfs(r):
    global count
    if r == N:      
        count += 1
        return
    
    for c in range(N):
        if visited[r][c] == 10**9:
            visited[r][c] = -1
            for dir in range(3):
                nr = r
                nc = c
                
                while  1:
                    nr += dr[dir]
                    nc += dc[dir]
                    if 0 <= nr < N and 0 <= nc < N:
                        if visited[nr][nc] > r+1:              
                            visited[nr][nc] = r+1 # 우주괴물 광선발사
                    else:
                        break

     
            dfs(r+1)
            visited[r][c] = 10**9
            for dir in range(3): # 광선 원복
                nr = r
                nc = c

                while  1:
                    nr += dr[dir]
                    nc += dc[dir]
                    if 0 <= nr < N and 0 <= nc < N:
                        if visited[nr][nc] == r+1:              
                            visited[nr][nc] = 10**9 # 우주괴물 광선발사
                    else:
                        break
dfs(0)
print(count)          
            

    # for dir in range(3):
    #     nr = r + dr[dir]
    #     nc = c + dc[dir]

    #     while 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
    #         visited[nr][nc] = 1
    #         nr =+ dr[dir]
    #         nc =+ dc[dir]

            # dfs(nr, nc) #문제?
            # # visited[r][c] = 0


