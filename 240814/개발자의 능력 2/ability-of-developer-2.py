devs, LENGTH = list(map(int, input().split())), 6
devs.sort()

team_1 = devs[0] + devs[5]
team_2 = devs[1] + devs[4]
team_3 = devs[2] + devs[3]

max_sum = max(team_1, team_2, team_3)
min_sum = min(team_1, team_2, team_3)

print(max_sum - min_sum)