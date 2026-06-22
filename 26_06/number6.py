number = int(input())
count = 1 # 성립하는 개수 count
front = 1 # front index
last = 1 # last index
sum = 1 # 합 체크

while last != number :
    if sum == number : # 정답 케이스
        count += 1
        last += 1
        sum += last # sum도 증가한만큼 더해서 체크해야 함.
    elif sum > number :
        sum -= front
        front += 1
    else : 
        last += 1
        sum += last
print(count)