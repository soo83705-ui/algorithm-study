#첫쨰줄:수열의 크기 n이 주어짐 
n = int(input())

#둘쨰줄:수열에 포함되는 수 많아서 리스트로 묶어봄 
A = list(map(int,input().split())) 

#셋째줄 : X
X = int(input())

count = 0 #(a,b)쌍의 갯수 0개로 설정 . 
for a in range(n):  #a 변수가 n번 꺼내지는동안 
      for b in range(n): #b변수도 n번 꺼내짐
            if a + b == X:  #변수 a+b의 합이 X와 같아지면
                  count += 1  #(a,b)쌍의 개수가 +1씩 높아짐 
print(count-1) #개수 "0" 빼기 