T = int(input())

for tc in range(1,T+1):
    A,B,C = map(int,input().split())  # 세 개의 자연수


    cnt =0
    if B >= C:  # 고쳐야하는 경우

        cnt += (B-C+1)

        B = B- (B-C+1)



    if A >= B:  # 고쳐야하는 경우

        cnt += (A-B+1)
        A = A - (A-B+1)


    if A >= 1 and B >= 1 and C >= 1:
        print(f'#{tc} {cnt}')

    else:
        print(f'#{tc} -1')





