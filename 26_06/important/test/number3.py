import random
import time

# 테스트 데이터 개수
suNo = 100      # 숫자 100개
quizNo = 100    # 질문 100개

# 랜덤 숫자 100개 생성
numbers = [random.randint(1, 100) for _ in range(suNo)]

# 랜덤 쿼리 100개 생성
queries = []

for _ in range(quizNo):
    s = random.randint(1, suNo)
    e = random.randint(1, suNo)

    # s가 e보다 크면 바꿔줌
    if s > e:
        s, e = e, s

    queries.append((s, e))


print("numbers:")
print(numbers)

print("\nqueries:")
print(queries)


# -----------------------------
# 1. 합 배열을 미리 계산하지 않은 경우
# -----------------------------
start = time.perf_counter()

slow_answers = []

for s, e in queries:
    result = 0

    for x in range(s - 1, e):
        result += numbers[x]

    slow_answers.append(result)

end = time.perf_counter()

print("\n직접 더하기 결과:")
print(slow_answers)
print("직접 더하기 실행 시간:", end - start)


# -----------------------------
# 2. 합 배열을 미리 계산한 경우
# -----------------------------
start = time.perf_counter()

prefix_sum = [0]
temp = 0

for num in numbers:
    temp += num
    prefix_sum.append(temp)

fast_answers = []

for s, e in queries:
    fast_answers.append(prefix_sum[e] - prefix_sum[s - 1])

end = time.perf_counter()

print("\n누적합 결과:")
print(fast_answers)
print("누적합 실행 시간:", end - start)


# -----------------------------
# 3. 두 결과가 같은지 확인
# -----------------------------
print("\n결과 일치 여부:", slow_answers == fast_answers)