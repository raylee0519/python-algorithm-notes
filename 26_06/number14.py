from queue import PriorityQueue
num = int(input())

My = PriorityQueue()

for i in range(num) : 
    request = int(input())
    if request == 0 :
        if My.empty() :
            print("0\n")
        else :
            temp = My.get()
            print(str(temp[1]) + "\n")
    else :
        My.put((abs(request), request))