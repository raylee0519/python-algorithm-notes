n, m = map(int, input().split())

dna = input()[:n]
need = list(map(int, input().split()))  # A C G T 순서

answer = 0

for start in range(n - m + 1):
    part = dna[start:start + m]

    a_count = part.count("A")
    c_count = part.count("C")
    g_count = part.count("G")
    t_count = part.count("T")

    if (
        a_count >= need[0]
        and c_count >= need[1]
        and g_count >= need[2]
        and t_count >= need[3]
    ):
        answer += 1

print(answer)