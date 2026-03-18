def subset(cnt, prev):
    if sum(path) == S and path:
        ans.append(path[:])

    for i in range(prev, N):
        path.append(num_lst[i])
        subset(cnt + 1, i +1)
        path.pop()


N, S = map(int, input().split())
num_lst = list(map(int, input().split()))
path = []
ans = []

subset(0,0)
print(len(ans))

