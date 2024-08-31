a, b, c = map(int, input().split())

dist1 = b - a
dist2 = c - b

count = 0
while dist1 > 1 or dist2 > 1:
    if dist1 > dist2:
        a = (b + c) // 2
    else:
        c = (a + b) // 2

    dist1 = b - a
    dist2 = c - b
    count += 1

print(count)