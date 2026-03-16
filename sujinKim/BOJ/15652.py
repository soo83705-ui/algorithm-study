### 중복조합이니까 앞에서부터의 수를 갱신하면 됨
### 중복이니까 방문배열 불필요
N,M = map(int,input().split())

arr = list(range(1,N+1))
result = [0]*M

def recur(start,index):
    if index == M:
        print(*result)
        return
    for i in range(start,N):
        result[index] = arr[i]
        recur(i,index+1)

recur(0,0)



