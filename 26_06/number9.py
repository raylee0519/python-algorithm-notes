n, m = map(int, input().split())
dna = input()
dna_list = list(map(int, input().split())) # a,c,g,t 순서대로 저장 / 최소 개수 세팅

current = [0,0,0,0]

def add_char(ch) : # 실제로 넣었을 때 현재 개수를 측정
    if ch == "A" : 
        current[0] += 1
    elif ch == "C" : 
        current[1] += 1 
    elif ch == "G" : 
        current[2] += 1 
    elif ch == "T" : 
        current[3] += 1 

def remove_char(ch) : # 슬라이딩 윈도우로 인해 빠지는 것을 계산
    if ch == "A" : 
        current[0] -= 1
    elif ch == "C" : 
        current[1] -= 1 
    elif ch == "G" : 
        current[2] -= 1 
    elif ch == "T" : 
        current[3] -= 1 

def is_valid(): # 최소 개수 성립했는지 체크
    for i in range(4):
        if current[i] < dna_list[i]:
            return False
    return True

# 첫 번째 윈도우 세팅 (선택한 개수만큼 단어를 증가)
for i in range(m):
    add_char(dna[i])

answer = 0

if is_valid(): # 최소 개수 성립하면 answer + 1
    answer += 1

# 윈도우 이동
for right in range(m, n): # 부분 문자열 길이부터 -> 전체 문자열 길이까지
    print("right", right)
    left = right - m # left 계산
    print("left", left)

    remove_char(dna[left])   # 빠지는 문자
    add_char(dna[right])     # 새로 들어오는 문자

    if is_valid():
        answer += 1

print(answer)