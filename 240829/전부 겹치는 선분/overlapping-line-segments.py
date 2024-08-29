def does_intersect(start, end, lines):
    for k in range(start, end + 1):
        if all(line[0] <= k <= line[1] for line in lines):
            return True
    return False


n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

start = min(line[0] for line in lines)
end = max(line[1] for line in lines)

result = does_intersect(start, end, lines)
if result:
    print("Yes")
else:
    print("No")