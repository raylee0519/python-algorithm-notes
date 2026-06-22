n = int(input())
nsum = int(input())
m = list(map(int, input().split())) # materials
m.sort() # 정렬 필요

# index set
x = 1
y = n-1
count = 0

while x < y :
    if m[x] + m[y] < nsum :
        x += 1
    elif m[x] + m[y] > nsum :
        y -= 1
    else :
        count += 1
        x += 1
        y -= 1

print(count)