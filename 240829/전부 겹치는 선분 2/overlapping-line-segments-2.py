def does_intersect(cur_idx, lines, n):
    max_x1 = 0
    min_x2 = float("inf")
    
    for i in range(n):
        if i == cur_idx:
            continue

        line = lines[i]
        max_x1 = max(max_x1, line[0])
        min_x2 = min(min_x2, line[1])
    
    if min_x2 >= max_x1:
        return True
    
    return False
        


n = int(input())
lines = [[int(num) for num in input().split()] for _ in range(n)]

result = False
for i, line in enumerate(lines):
    if does_intersect(i, lines, n):
        result = True
        break

if result:
    print("Yes")
else:
    print("No")