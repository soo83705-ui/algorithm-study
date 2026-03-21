N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터 쌍의 수 간선 수

adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(node):
    visited[node] = 1
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(1)

print(sum(visited)-1)



    
