import math

N = int(input())
hills = [int(input()) for _ in range(N)]
hills.sort()

min_height, max_height = min(hills), max(hills)

answer = math.inf
for height in range(min_height, max_height + 1):
    total_cost = 0

    if (max_height - height) - (min_height + height) <= 17:
        for hill in hills:
            cost = pow(height,2) * 2

            if hill == min_height or hill == max_height:
                total_cost += cost
            
        answer = min(answer, cost)

print(answer)