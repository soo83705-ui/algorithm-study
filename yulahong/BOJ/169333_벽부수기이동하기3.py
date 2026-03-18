# NxM행렬 맵, 상하좌우 이동
# 0 이동 1은 벽
# 1,1에서 N,M까지 최단경로로 이동 -> bfs
# 이동하지 않고 같은 칸에 머무르기 가능
# 낮과 밤 존재 이동할 때마다 낮과 밤 바뀜
# 이동하지 않아도 낮과 밤 바뀜
# 벽부수기 가능 - k개까지 
# 낮에만 부수기 가능

from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]