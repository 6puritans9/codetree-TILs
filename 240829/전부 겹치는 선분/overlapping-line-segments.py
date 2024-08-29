def does_intersect(start, end, lines):
    for k in range(start, end + 1):
        for line in lines:
            if line[0] > k or k < line[1]:
                break
        return True
    
    return False


n = int(input())
lines = [tuple(int(num) for num in input().split()) for _ in range(n)]

start, end = min(lines[0]), max(lines[1])
intersection = does_intersect(start, end, lines)
if intersection:
    print("Yes")
else:
    print("No")