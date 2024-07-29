def in_range(x, y, n):
    return x>=0 and x<n and y>=0 and y<n

n = int(input())

table = []
for _ in range(n):
    row = [int(num) for num in input().split()]
    table.append(row)

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
result = 0

for x in range(n):
    for y in range(n):
        count = 0

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
          
            if in_range(nx, ny, n) and table[nx][ny]:
                count += 1
        if count >= 3:
            result += 1

print(result)