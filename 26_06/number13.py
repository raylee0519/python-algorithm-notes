from collections import deque
num = int(input())
My = deque()

for i in range(1, num+1) :
    My.append(i)

while len(My) > 1 :
    My.popleft()
    My.append(My.popleft())

print(My[0])