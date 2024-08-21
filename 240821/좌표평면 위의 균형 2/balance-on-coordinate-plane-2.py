N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

dots.sort(key = lambda x:x[0])
min_x, max_x = dots[0][0], dots[-1][0]

dots.sort(key = lambda x:x[1])
min_y, max_y = dots[0][1], dots[-1][1]

max_quarter = float("inf")
for i in range(min_x, max_x + 1):
    cur_max_quarter = 0

    for j in range(min_y, min_y + 1):
        # get the actual quarter which dots are in
        q1, q2, q3, q4 = 0, 0, 0, 0
        for dot in dots:
            x, y = dot

            if x > i and y > j:
                q1 += 1
            elif x < i and y > j:
                q2 += 1
            elif x < i and y < j:
                q3 += 1
            elif x > i and y < j:
                q4 += 1
            
        cur_max_quarter = max(q1,q2,q3,q4)
    max_quarter = min(max_quarter, cur_max_quarter)

print(max_quarter)