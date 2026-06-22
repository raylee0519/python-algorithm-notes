# 합 배열을 미리 계산하지 않았을 경우 (mine)
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
temp = 0

for i in range(quizNo) :
    s, e = map(int, input().split())
    for x in range(s-1, e) : 
        result += numbers[x]
    print(result)
    result = 0