import math

need = [0 for _ in range(10)]
only_69 = [0, 0]
number = list(input())

for n in number :
    if n == '6' :
        only_69[0] += 1
    elif n == '9' :
        only_69[1] += 1
    else :
        need[int(n)] += 1

# 6, 9는 뒤집어서 쓸 수 있기 때문에 필요한 6, 9 개수의 합의 절반만큼의 세트가 필요함
# 나머지 숫자는 필요한 개수만큼 세트가 필요함
# 따라서 이 두 수의 max가 필요한 세트 개수가 된다.
print(max(math.ceil(sum(only_69)/2), max(need)))