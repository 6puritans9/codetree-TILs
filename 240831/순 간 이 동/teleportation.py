A, B, x, y = map(int, input().split())

dist1 = abs(A-B)
dist2 = abs(x-A) + abs(y - B)
dist3 = abs(y-A) + abs(x-B)

print(min(dist1, dist2, dist3))