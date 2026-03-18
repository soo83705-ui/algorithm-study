low_lst = []
ans = []
for _ in range(9):
    low_lst.append(int(input()))


def recur(cnt, prev):
    if cnt == 7 and sum(ans) == 100:
        for j in sorted(ans):
            print(j)
        exit()
        return


    for i in range(prev, 9):
        ans.append(low_lst[i])
        recur(cnt+1, i+1)
        ans.pop()

recur(0,0)



