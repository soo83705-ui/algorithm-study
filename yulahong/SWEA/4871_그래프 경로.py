# 첫줄에 케이스 개수: T
# 다음줄부터 V와 E
# E개의 줄에 걸쳐 도착노드로의 간선 정보
# E개의 줄 이후에 출발 노드 S, 도착노드 G

# S가 G로 가는 경로 있으면 1 없으면 0


from collections import deque

T = int(input)

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V + 1)] #인접리스트
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)  

    S, G = map(int, input().split()) #출발노드와 도착노드

    q = deque([S])
    visited = [0] * [V+1]
    visited[S] = 1

    ans = 0 # 기본값 0으로 주기(경로 없을 때)

    while q:
        cn = q.popleft()

        if cn == G:
            ans = 1
            break

        for nn in adj[cn]:
            if not visited[nn]:
                visited[nn] = 1
                q.append(nn)
    
    print(f'#{tc} {ans}')
