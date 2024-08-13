devs = tuple(map(int, input().split()))
length = len(devs)
total_sum = sum(devs)

min_diff = float("inf")
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            team1_sum = devs[i] + devs[j] + devs[k]
            team2_sum = total_sum - team1_sum
            cur_diff = abs(team1_sum - team2_sum)

            min_diff = min(min_diff, cur_diff)

print(min_diff)