devs = list(map(int, input().split()))
total_sum = sum(devs)

team1 = 0
team2 = 0
team3 = 0

min_diff = float("inf")
for i in range(5):
    for j in range(5):
        if i == j:
            break
        
        team1 = devs[i] + devs[j]

        for k in range(5):
            for l in range(5):
                if k == l:
                    break
                
                team2 = devs[k] + devs[l]

                if team1 == team2:
                    break
        
                single_dev = total_sum - (team1 + team2)

                max_devs = max(team1, team2, single_dev)
                min_devs = min(team1, team2, single_dev)

                min_diff = min(min_diff, max_devs - min_devs)

print(min_diff)