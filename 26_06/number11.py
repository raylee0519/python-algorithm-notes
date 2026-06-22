n = int(input())
A = []

for i in range(n):
    a = int(input())
    A.append(a)

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    su = A[i]

    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"

        stack.pop()
        answer += "-\n"

    else:
        top = stack.pop()

        if top != su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)