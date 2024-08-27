import math

N = int(input())
hills = [int(input()) for _ in range(N)]

min_height, max_height = min(hills), max(hills)

answer = math.inf
for height in range(min_height, max_height + 1):
    if (max_height - height) - (min_height + height) <= 17:
        cost = pow(height,2) * 2
            
        answer = min(answer, cost)

print(answer)