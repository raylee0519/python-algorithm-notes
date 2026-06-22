n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
result = 0

for i in range(n) :
    find = nlist[i]
    x = 0
    y = n-1
    while x < y :
        if nlist[x] + nlist[y] == find :
            if x != i and y != i :
                result += 1
                break
            elif x == i :
                x += 1
            elif y == i :
                y -= 1
        elif nlist[x] + nlist[y] < find :
            x += 1
        else :
            y -= 1
print(result)