N = int(input())
op_hour = [tuple(int(num) for num in input().split()) for _ in range(N)]

max_hour = 0
for i in range(N):
    hour_table = [0] * (1000 + 1)

    for j in range(N):
        if i ==j:
            continue

        start, end = op_hour[j]

        for k in range(start, end):
            hour_table[k] = 1

        max_hour = max(max_hour, sum(hour_table))

print(max_hour)