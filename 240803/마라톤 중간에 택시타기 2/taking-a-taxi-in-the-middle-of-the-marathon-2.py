N = int(input())
checkpoints = [list(map(int, input().split())) for _ in range(N)]
total_dist = 0

for i in range(N - 1):
    x1, y1 = checkpoints[i][0], checkpoints[i][1]
    x2, y2 = checkpoints[i+1][0], checkpoints[i+1][1]   
    
    total_dist += abs(x2-x1) + abs(y2-y1)

min_dist = total_dist
for i in range(1, N-1):
    x1, y1 = checkpoints[i-1][0], checkpoints[i-1][1]
    x2, y2 = checkpoints[i][0], checkpoints[i][1]
    x3, y3 = checkpoints[i+1][0], checkpoints[i+1][1]
    
    skip_dist = (abs(x2-x1) + abs(y2-y1)) + (abs(x3-x2) + abs(y3-y2))
    alt_dist = abs(x3-x1) + abs(y3-y1)
    min_dist = min(min_dist, total_dist - skip_dist + alt_dist)

print(min_dist)