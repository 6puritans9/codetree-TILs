a, b, c = map(int, input().split())
dist1 = abs(b-a)
dist2 = abs(c-b)

moves = 0
while dist1 != 1 or dist2 != 1:
    if dist1 > dist2:
        c = a + 1
        b, c = c, b
    elif dist1 < dist2:
        a = c - 1
        a, b = b, a

    dist1 = abs(b - a)
    dist2 = abs(c - b)
    moves += 1

print(moves)