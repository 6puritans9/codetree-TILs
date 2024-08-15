N = int(input())
dots = [[int(num) for num in input().split()] for _ in range(N)]

area = float("inf")
for i in range(N):
    min_width = float("inf")
    min_height = float("inf")

    xs = []
    ys = []
    for j in range(N):
        if i == j:
            continue

        x, y = dots[j]
        xs.append(x)
        ys.append(y)

    cur_width = max(xs) - min(xs)
    cur_height = max(ys) - min(ys)

    min_width = min(min_width, cur_width)
    min_height = min(min_height, cur_height)

    area = min(area, min_width * min_height)

print(area)