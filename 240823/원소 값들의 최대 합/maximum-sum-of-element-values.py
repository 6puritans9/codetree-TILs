n, m = map(int, input().split())
sequence = list(map(int, input().split()))

total = 0
for i in range(n):
    current_total = 0
    new_index = i

    for turn in range(m):
        num = sequence[new_index]
        new_index = num - 1

        current_total += num
    
    total = max(total, current_total)

print(total)