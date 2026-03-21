import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수
visited = [0]*(N+1)
adj = [[] for _ in range(N+1)]
cnt = 0

for i in range(M):
    u, v = map(int, input().split())

    adj[u].append(v)
    adj[v].append(u)

def dfs(node):
    visited[node] = 1
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor)

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)
