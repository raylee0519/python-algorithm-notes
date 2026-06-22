size, qiz = map(int, input().split())

result = []
result_sum = [[0] * (size + 1) for _ in range(size + 1)]

for i in range(size) :
    j_group = list(map(int, input().split()))
    result.append(j_group)

print(result)

for i in range(1, size + 1) :
    for j in range(1, size + 1) :
        result_sum[i][j] = result_sum[i][j-1] + result_sum[i-1][j] - result_sum[i-1][j-1] + result[i-1][j-1]
print(result_sum)

for _ in range(qiz) :
    x1, y1, x2, y2 = map(int, input().split())
    result_no = result_sum[x2][y2] - result_sum[x1-1][y2] - result_sum[x2][y1-1] + result_sum[x1-1][y1-1]
    print(result_no)