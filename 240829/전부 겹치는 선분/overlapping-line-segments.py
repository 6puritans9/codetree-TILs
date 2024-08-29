def does_intersect(start, end, lines):
    for k in range(start, end + 1):
        if all(k for k in lines):
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