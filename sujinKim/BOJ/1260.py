# DFS와 BFS 

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성 
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료 
# 정점 번호 1~N번까지

# 첫 번쨰 : DFS 
# 두 번째 : BFS 

N,M,V = map(int,input().split())  # 정점의 개수 : N, 간선의 개수 :M , 탐색시작정점번호 :V
arr = [list(map(int,input().split())) for _ in range(M)]  # 간선이 연결하는 두 정점의 번호 

print(result)
print(result1)

# DFS : 끝까지 갔다가 나오기
# BFS : 주변 다 챙겨서 들어가기 
result = [0]*N  # 인덱스 : idx
result1 = [0]*N

# DFS
def DFS(idx):
    for i in range(M): # arr의 0행부터 돌거야
        if arr[i][0] == V: # 시작할 정점을 찾았다면 
            result[idx] = V # 연결된 정점을 넣어줘 ex. 1 2까지 넣었고 이제 2부터 다시 찾아야지
            result[idx+1] = arr[i][1] # result의 그 다음칸에 연결된 애를 넣어줌 
            V = arr[i][1]  # 그리고 시작정점 다시 정해줘 
    DFS(idx+2) # 그 다음에 idx+1 즉, 옆자리 호출(?)


DFS(0)


def BFS(idx1):
    result[idx1] = V
    for i in range(M):
        if arr[i][0] == V: #시작할 정점을 찾았다면 
            result1[idx1+1] = arr[i][1] # 시작정점이랑 연결된애들 싹 차례로 넣기 
        if arr[i][0] == result1[idx1+1]:  # 넣었던것중 앞에꺼라면
     
            result1[idx1+2] = arr[i][1]  # 연결된애들 넣어줌 
BFS(0)


           



    
