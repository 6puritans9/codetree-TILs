n = int(input())
dots = [tuple(int(num) for num in input().split()) for _ in range(n)]

min_squared_dist = float("inf")
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = dots[i]
        x2, y2 = dots[j]

        diff_x = abs(x1 - x2)
        diff_y = abs(y1 - y2)

        min_squared_dist = min(min_squared_dist, pow(diff_x, 2) + pow(diff_y, 2))

print(min_squared_dist)