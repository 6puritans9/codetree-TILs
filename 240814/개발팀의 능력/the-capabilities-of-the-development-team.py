devs = list(map(int, input().split()))
total_sum = sum(devs)

# team1 = 0
# team2 = 0

min_diff = float("inf")
for i in range(5):
    for j in range(i+1, 5):
        
        for k in range(5):
            for l in range(k+1, 5):
                if i == k or i == l or j == k or j== l:
                    break

                team1 = devs[i] + devs[j]
                team2 = devs[k] + devs[l]
                single_dev = total_sum - (team1 + team2)

                if team1 == team2 or team2 == single_dev or single_dev == team1:
                    break

                max_devs = max(team1, team2, single_dev)
                min_devs = min(team1, team2, single_dev)

                min_diff = min(min_diff, max_devs - min_devs)

if min_diff == float("inf"):
    print(-1)
else:
    print(min_diff)