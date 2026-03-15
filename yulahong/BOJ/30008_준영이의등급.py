
lst = []

while True:
    a = int(input())
    if a == -1:
        break
    lst.append(a)


ans = sum(lst)
print(ans)
