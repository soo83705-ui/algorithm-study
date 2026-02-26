from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self,item):
        self.dq.append(item)
    def empty(self):
        return not self.dq
    def size(self):
        return len(self.dq)
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")

        return self.dq[0]


n, k = tuple(map(int, input().split()))

# Please write your code here.
q = Queue()

for i in range(1,n+1):
    q.push(i)  #1번부터 q에 넣는다. 

while q.size() > 1:
    for _ in range(k-1): #k-1번 다 돌고 나면, 우리가 죽이고 싶었던 k번째 사람이 자연스럽게 큐의 맨 앞에 옴. 
        q.push(q.front())  #맨 앞 사람을 확인해서 뒤에 줄 세우기 
        q.pop() #맨 앞에 있던 것을 뒤로 보내고 pop을 해서 앞에 것을 없앰 
###collections.deque와 queue 클래스에서는 동작이 조금 다름 
#popleft는 이름 그대로 왼쪽에서 데이터를 쏙 뺴오는 함수이다. 그래서 이름은 pop이지만
#실제로는 가장 오래된 데이터를 지우게 된다. 
    print(q.front(),end=" ") #맨 앞이 누구인지 확인해서 화면에 출력
    q.pop() #확인하고 큐에서 제거 

print(q.front(),end=" ")


    

