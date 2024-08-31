N = int(input())
pairs = [[int(num) for num in input().split()] for _ in range(N)]

count1 = 0
count2 = 0
for pair in pairs:
    a, b = pair
    if a == b:
        continue

    if a > b:
        count1 += 1
    else:
        count2 += 1

print(max(count1, count2))