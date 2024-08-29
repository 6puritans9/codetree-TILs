def does_intersect(start, end, lines):
    for line in lines:
        if line[0] > k or k < line[1]:
            return False

    return True


n = int(input())
lines = [tuple(int(num) for num in input().split()) for _ in range(n)]

start, end = min(lines[0]), max(lines[1])
intersection = False

for k in range(start, end + 1):
    intersection = does_intersect(start, end, lines)
    if intersection:
        break

if intersection:
    print("Yes")
else:
    print("No")