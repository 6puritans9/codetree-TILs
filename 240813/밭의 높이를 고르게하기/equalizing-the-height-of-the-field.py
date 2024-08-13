N, H, T = tuple(map(int, input().split()))
heights = list(map(int, input().split()))

min_cost = float("inf")
for i in range(N - T + 1):
    cur_cost = 0
    for j in range(i, i+T):
        diff = abs(H - heights[j])
        cur_cost += diff
    
    min_cost = min(min_cost, cur_cost)

print(min_cost)