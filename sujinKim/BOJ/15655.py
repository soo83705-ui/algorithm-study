# 조합
# import sys
# sys.stdin = open('input.txt')

N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result = [0]*M

def DFS(start,index):

    if index == M:
        print(*result)
        return
    for i in range(start,N):
        result[index] = arr[i]
        DFS(i+1,index+1)  # start값에 i+1을 해야 옆으로 가지 !!!
        result[index] = 0 # 마지막에 넣어줬던 수를 빼줘야 다음게 들어갈거 아니야


DFS(0,0)



